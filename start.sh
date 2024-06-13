#!/bin/bash

# Exécutez getImagesApi.py
python3 getImagesApi.py

# Démarrez l'application avec gunicorn
gunicorn -w 4 -b 0.0.0.0:80 mainAI:app