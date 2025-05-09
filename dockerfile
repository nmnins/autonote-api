# Étape 1 : utiliser une image Python légère
FROM python:3.13.3-slim

# Étape 2 : définir le répertoire de travail
WORKDIR /app

# Étape 3 : copier requirements d’abord pour profiter du cache
COPY requirements.txt .

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Étape 5 : copier le reste du code
COPY . .

# copie du script wait attente de la db
RUN chmod +x /app/wait-for-it.sh

# Étape 6 : exposer le port de l’API
EXPOSE 8000

# Étape 7 : commande de lancement avec Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
