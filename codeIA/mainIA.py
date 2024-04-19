import cv2
import sys
import requests
from simple_facerec import SimpleFacerec

## Affichage du score serait intérressant injection de dépendance

## for exec:
## IARecognitionSystem/codeIA/mainIA.py "20240119_143216.jpg"
# Encode images from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("./Images/")

#Old version
#sfr.load_encoding_images("C:/Users/natha/Desktop/testFramePython/IARecognitionSystem/codeIA/Images/")
#image_path = shared_arg1
#frame = cv2.imread(image_path)

# URL API
# url = "http://localhost:8081/v1/person"

# # Si votre API nécessite un token JWT pour l'authentification, ajoutez-le dans les headers
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8tWEpRYkVvaG14TzNEWFU5MGJlZCJ9.eyJpc3MiOiJodHRwczovL2Rldi0zamE3M3dwZnAxajZ1emVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJlQWY4ejR2UzNCNDdMR2F0VG4zNHEzOElSZEpyTk52Y0BjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly90b3hpYXBpLyIsImlhdCI6MTcxMzQ4MTAwNSwiZXhwIjoxNzEzNTY3NDA1LCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJhenAiOiJlQWY4ejR2UzNCNDdMR2F0VG4zNHEzOElSZEpyTk52YyJ9.OEKMrxZUyPOjxMnE8chRT3fOCJKjn8BCrGxnwcjXVzZ1q0Q_FwWLPXgV1eT9JcAn1wxeKTBdPTZFMQNxom73wPc-mRUlupsOh3ByNVxt6P951_VCtym2oYmo921xhS_0fcXRuw4nzSAcDyfl0uFo6jnjX203F1CrU26Ds22sGQ0vMRZm8gi24t4SVy9l4t5MudVvcPcd5zSCkTfAarlqx_yh6A3AbBQVWIAg313-qYnHszsHZXDR_e15qFenrGRHaywNKoZ7btlOVxx_z5s1-f7IICafwHMUMno2RimSxIvWKWQ8fKHlZUonYG57G-xwT368Yu2Vi3MVgmfufUF4Mw"
# }

# response = requests.get(url, headers=headers)

# # 200 if connection work
# if response.status_code == 200:
#     # Convertir la réponse en format JSON si l'API renvoie du JSON
#     data = response.json()
#     print("Données reçues de l'API :", data)

#     # Récupérer le tableau de bytes de l'API
#     # image_bytes = bytes.fromhex(data["image"])  # Supposons que les données bytes sont dans la clé "image_data"

#     # # Convertir les bytes en un tableau NumPy
#     # nparr = np.frombuffer(image_bytes, np.uint8)

#     # # Décoder l'image à l'aide de OpenCV
#     # frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
# else:
#     print("Échec de la requête. Code d'état :", response.status_code)

# Read the image from a file
image_path = sys.argv[1]  # Get the image path from command line arguments
frame = cv2.imread(image_path)

# Face detection
face_locations, face_names = sfr.detect_known_faces(frame)
for face_loc, name in zip(face_locations, face_names):
    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

    # Shows the person's name
    cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)

    # Displays the rectangle around the detected face
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

# Allows you to open the small window (camera return)
cv2.imshow("Frame", frame)
cv2.waitKey(0)  # Wait for a key press before closing the image
cv2.destroyAllWindows()
