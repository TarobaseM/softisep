# Utiliser une image de base officielle Python
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel Django va s'exécuter
EXPOSE 8080

# Définir la commande pour démarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

