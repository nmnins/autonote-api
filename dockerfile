# J'utilise une image python légère 
FROM python:3.13.3-slim

# Je définis le répertoire de travail
WORKDIR /app

# Je copie requirements.txt qui contient les dépendances
COPY requirements.txt .

# J'installe les dépendances sans stocker de cache local (réduit le poids de l'image)
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Je copie le reste du code
COPY . .

# J'expose le port de l'api 
EXPOSE 8000

# Je lance l'app avec uvicorn 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
