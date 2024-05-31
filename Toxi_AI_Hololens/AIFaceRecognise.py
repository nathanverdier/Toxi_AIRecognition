import cv2
import sys
import numpy as np
import requests
import os
from flask import Flask, request, jsonify
import face_recognition
import glob
import argparse
import json

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        # Load images from images path folder
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encodage des images trouvées.".format(len(images_path)))

        # Store image encodings with their names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the file name only from the initial file path
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)

            # Gets the encodings
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store the file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("L'encodages des images est chargée")


    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

        # Find all faces and their face encodings in the current video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)

        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            
            # Check if the face matches the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknow"

            # Or rather, use the known face with the smallest distance from the new face or the highest match percentage
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert to array to quickly adjust coordinates with frame resizinge
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names

    def detect_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)

        # Convert to array to quickly adjust coordinates with frame resizing
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Detect faces in an image.')
parser.add_argument('image_path', help='Path to the image file.')
args = parser.parse_args()

# Load the image
image = cv2.imread(args.image_path)

# Check if the image was loaded successfully
if image is None:
    print(f'Error: Could not load image from {args.image_path}')
    exit(1)

sfr = SimpleFacerec()

# Detect faces
face_locations = sfr.detect_faces(image)

face_locations = face_locations.tolist()

face_locations_named = [{'x1': loc[3], 'x2': loc[1], 'y1': loc[0], 'y2': loc[2]} for loc in face_locations]

# Create a response
response = {
    'face_locations': face_locations_named,
}

print(json.dumps(response))