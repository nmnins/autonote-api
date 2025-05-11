#!/bin/bash

# MAJ système
sudo apt update -y
sudo apt upgrade -y

# Dépendances pour ajouter le repo Docker
sudo apt install -y ca-certificates curl gnupg lsb-release

# Ajouter la clé GPG officielle de Docker
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Ajouter le dépôt Docker officiel
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Mettre à jour les dépôts et installer Docker
sudo apt update -y
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Démarrer Docker
sudo systemctl enable docker
sudo systemctl start docker

# clone de mon dépot
cd /home/ubuntu
git clone https://github.com/nmnins/autonote-api.git
cd autonote-api

# 6. Lancer l'app (en arrière-plan)
docker compose up -d
