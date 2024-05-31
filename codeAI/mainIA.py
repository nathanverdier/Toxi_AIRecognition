import cv2
import sys
import numpy as np
import requests
import os
from simple_facerec import SimpleFacerec
from flask import Flask, request, jsonify

# Vérifiez que le dossier Images existe et contient des fichiers
if not os.path.exists("./Images/") or not os.listdir("./Images/"):
    print("The pictures folder is empty or does not exist.")
    sys.exit(1)

sfr = SimpleFacerec()
sfr.load_encoding_images("./Images/")

app = Flask(__name__)

## for exec:
## IARecognitionSystem/codeIA/mainIA.py "20240119_143216.jpg"
# Encode images from a folder

@app.route('/detect_faces', methods=['POST'])
def detect_faces():
    
    image_file = request.files.get('image')
    if not image_file:
        return jsonify({'error': 'No image file provided'}), 400

    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Détecter les visages
    face_locations, face_names = sfr.detect_known_faces(image)
    
    face_locations = face_locations.tolist()

    face_locations_named = [{'x1': loc[3], 'x2': loc[1], 'y1': loc[0], 'y2': loc[2]} for loc in face_locations]

    # Créer une réponse
    response = {
        'face_locations': face_locations_named,
        'face_names': face_names,
    }

    return jsonify(response)

@app.route('/detect_only_faces', methods=['POST'])
def detect_only_faces():
    
    image_file = request.files.get('image')
    if not image_file:
        return jsonify({'error': 'No image file provided'}), 400

    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Détecter les visages
    face_locations = sfr.detect_faces(image)
    
    face_locations = face_locations.tolist()

    face_locations_named = [{'x1': loc[3], 'x2': loc[1], 'y1': loc[0], 'y2': loc[2]} for loc in face_locations]

    # Créer une réponse
    response = {
        'face_locations': face_locations_named,
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
# Read the image from a file
# image_path = sys.argv[1]  # Get the image path from command line arguments
# frame = cv2.imread(image_path)

# # Face detection
# face_locations, face_names = sfr.detect_known_faces(frame)
# for face_loc, name in zip(face_locations, face_names):
#     y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

#     # Shows the person's name
#     cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)

#     # Displays the rectangle around the detected face
#     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

# # Allows you to open the small window (camera return)
# cv2.imshow("Frame", frame)
# cv2.waitKey(0)  # Wait for a key press before closing the image
# cv2.destroyAllWindows()
