## 📝 AutoNote

AutoNote est une API REST légère construite avec FastAPI.  
Elle permet de créer, consulter et supprimer des messages via des endpoints HTTP.

Ce projet m’a permis de mettre en pratique les compétences suivantes :
- Tests unitaires automatisés avec Pytest
- Pipeline CI complet avec GitHub Actions
- Analyse de code (qualité, couverture, sécurité)
- Conteneurisation avec Docker
- Provisionnement cloud avec Terraform
- Déploiement d’une base PostgreSQL sur AWS RDS
- Déploiement de l’API sur AWS EC2

![CI](https://github.com/nmnins/autonote-api/actions/workflows/ci.yml/badge.svg)

### Fonctionnalités

- POST /notes : ajouter une note
- GET /notes : lister toutes les notes
- GET /notes/{id} : récupérer une note par ID
- PUT /notes/{id} : modifier une note
- DELETE /notes/{id} : supprimer une note

🔐 Toutes les routes sont sécurisées par une clé API transmise via le header x-api-key.

📦 Les données sont stockées dans une base PostgreSQL AWS RDS, provisionnée automatiquement via Terraform.

## Déploiement cloud automatisé (EC2 + RDS)

L’infrastructure est provisionnée automatiquement avec Terraform :

Une base de données PostgreSQL RDS

Une instance EC2 Ubuntu avec Docker + Docker Compose

Des security groups configurés

Un déploiement complet de l’application dès le démarrage de l’instance

🛠️ Le fichier .env est généré automatiquement via Terraform (avec injection sécurisée de API_KEY et DATABASE_URL).

Lancement de l’API : aucune action manuelle requise après terraform apply.

L'IP est communiquée après le terraform apply 

Pour accéder à l'API : http://<IP_PUBLIQUE_EC2>:8000
Et pour la doc interactive : http://<IP_PUBLIQUE_EC2>:8000/docs



## Installation locale

   ```bash
git clone https://github.com/nmnins/autonote-api.git
cd autonote-api
python -m venv env
source env/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
Sous Windows

   ```bash
env\Scripts\activate
```
##  Lancer les tests
   ```bash

pytest --cov=app --cov-report=term-missing
```

## Utilisation avec Docker
   ```bash

docker compose up –build
```

## Infrastructure AWS via Terraform

Le dossier terraform/ contient :
- Provisionnement automatique d'une instance RDS PostgreSQL
- Provisionnement d’une instance EC2 Ubuntu avec Docker
- Configuration des security groups

## CI & Sécurité

Le pipeline GitHub Actions vérifie à chaque push :
- Style et erreurs avec ruff
- Couverture des tests avec pytest-cov
- Vulnérabilités avec bandit et pip-audit
- Validité du Dockerfile avec docker build

📄 Pipeline : .github/workflows/ci.yml

## Structure du projet

```TEXT
autonote-api/
├── app/                  # Code principal (routes, modèles, logique)
├── tests/                # Tests unitaires
├── Dockerfile            # Image Docker de l'app
├── docker-compose.yml    # Définition de la stack 
├── .env                  # Variables d'environnement (non versionnées)
├── .env.example          # Exemple de fichier .env
├── terraform/            # Infrastructure RDS & EC2 (Terraform)
├── requirements*.txt     # Dépendances (prod/dev)
└── .github/
    └── workflows/
        └── ci.yml        # Pipeline CI GitHub Actions
```

## Sécurité

Les secrets (API_KEY, DATABASE_URL) sont injectés dynamiquement lors du déploiement via Terraform, dans un fichier .env non versionné.

L’accès à PostgreSQL RDS est restreint via les security groups : seules l’instance EC2 et ton IP personnelle (si configurée) peuvent y accéder.

Aucune donnée sensible (clé API, identifiants, URI) n’est stockée dans le dépôt Git.

Le fichier .env est exclu du contrôle de version via .gitignore.

Le provisioning complet (EC2 + RDS + configuration) est automatisé, limitant les risques d’erreurs humaines.

### Prochaines étapes

- [ ] Centralisation des logs + monitoring via CloudWatch
- [ ] Mise en place de tests d’intégration live
- [ ] Tests de montée en charge avec Locust

## À propos

Projet personnel pour expérimenter :
- Infrastructure as Code (Terraform)
- Conteneurisation (Docker & Compose)
- Déploiement cloud (EC2, RDS, IAM, Security Groups)
- CI/CD avec GitHub Actions

🎯 Objectif : construire une stack simple mais complète prête pour la production, avec bonnes pratiques DevOps.

