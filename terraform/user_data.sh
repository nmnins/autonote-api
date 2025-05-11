#!/bin/bash

# mise à jour des paquets
apt update -y
apt upgrade -y

# installation de docker et de git
apt install -y docker.io git

# je démarre docker
systemctl start docker
systemctl enable docker

# install de docker compose
DOCKER_CONFIG=/usr/libexec/docker/cli-plugins
mkdir -p $DOCKER_CONFIG
curl -SL https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/docker-compose
chmod +x $DOCKER_CONFIG/docker-compose

# clone de mon dépot
cd /home/ubuntu
git clone https://github.com/nmnins/autonote-api.git
cd autonote-api

# 6. Lancer l'app (en arrière-plan) fail pour le moment à lancer manuellement 
docker compose up -d
