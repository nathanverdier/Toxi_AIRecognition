# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de votre projet dans le conteneur
COPY . .

# Installer les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application fonctionne (si nécessaire)
EXPOSE 5000

# Commande par défaut pour exécuter l'application
CMD ["python", "app.py"]

