# Toxi_AIRecognition

## Installation
Create a Python virtual environment and download the project dependencies:  
```shell
python3 -m venv AIRecognitionEnv
source AIRecognitionEnv/bin/activate
pip install -r requirements.txt
```

## Use
Retrieve the images that detect people from the API `getImagesApi.py` then put them in the `Images/` folder, giving it the name that will be displayed when this person is detected.

## Run the script
```shell
python3 getImagesApi.py
cd codeAI
python3 mainIA.py Images/Remi.jpg
```
