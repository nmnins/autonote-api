#!/bin/bash


# désactiver le mode interactif
export DEBIAN_FRONTEND=noninteractive

# MAJ système
apt update -y
apt upgrade -y

# Docker + Git
apt install -y docker.io git

# Démarrage Docker
systemctl start docker
systemctl enable docker

# Docker Compose v2 install
DOCKER_CONFIG=/usr/libexec/docker/cli-plugins
mkdir -p $DOCKER_CONFIG
curl -SL https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/docker-compose
chmod +x $DOCKER_CONFIG/docker-compose

# Clone du repo
cd /home/ubuntu
git clone https://github.com/nmnins/autonote-api.git
cd autonote-api

# Création du fichier .env automatiquement (contenu injecté par Terraform)
cat <<EOF > .env
API_KEY=${API_KEY}
DATABASE_URL=${DATABASE_URL}
EOF

# Lancement de l’app
docker compose up -d
