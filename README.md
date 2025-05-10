# 📝 AutoNote

AutoNote est une API REST légère construite avec **FastAPI**.  
Elle permet de créer, consulter et supprimer des messages via des endpoints HTTP.

Ce projet m’a permis de mettre en pratique les compétences suivantes :

- Tests unitaires automatisés avec **Pytest**
- Pipeline CI complet avec **GitHub Actions**
- Analyse de code (qualité, couverture, sécurité)
- Conteneurisation avec **Docker**
- Provisionnement cloud avec **Terraform**
- Déploiement d’une base PostgreSQL sur **AWS RDS**
- Préparation au déploiement sur **EC2 AWS**

---

![CI](https://github.com/nmnins/autonote-api/actions/workflows/ci.yml/badge.svg)

---

## 🚀 Fonctionnalités

- `POST /notes` : ajouter une note
- `GET /notes` : lister toutes les notes
- `GET /notes/{id}` : récupérer une note par ID
- `PUT /notes/{id}` : modifier une note
- `DELETE /notes/{id}` : supprimer une note

🔐 Toutes les routes sont sécurisées par une **clé API** transmise via le header `x-api-key`.

📦 Les données sont stockées dans une **base PostgreSQL AWS RDS**, provisionnée automatiquement via Terraform.  

## ⚙️ Installation locale

```bash
git clone https://github.com/nmnins/autonote-api.git
cd autonote-api
python -m venv env
source env/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Sous Windows 
```bash
env\Scripts\activate
```

## Lancer les tests

```bash
pytest --cov=app --cov-report=term-missing
```

## Utilisation avec Docker

```bash
docker compose up --build
```

##  Infrastructure AWS via Terraform

Le dossier terraform/ contient :

Provisionnement automatique d'une instance RDS PostgreSQL

Configuration du Security Group AWS


## CI & Sécurité

Le pipeline GitHub Actions vérifie à chaque push :

Style et erreurs avec ruff

Couverture des tests avec pytest-cov

Vulnérabilités avec bandit et pip-audit

Validité du Dockerfile avec docker build

📄 Pipeline : .github/workflows/ci.yml


## Structure du projet
```text
autonote-api/
├── app/                  # Code principal (routes, modèles, logique)
├── tests/                # Tests unitaires
├── Dockerfile            # Image Docker de l'app
├── Docker-compose        # Définition de la stack 
├── .env                  # Variables d'environnement (non versionnées)
├── .env.example          # Exemple de fichier .env
├── terraform/            # Infrastructure RDS (Terraform)
├── requirements*.txt     # Dépendances (prod/dev)
└── .github/
    └── workflows/
        └── ci.yml        # Pipeline CI GitHub Actions
```


## Sécurité

Secrets gérés localement via .env

Accès PostgreSQL RDS restreint à l’IP personnelle

Aucune donnée sensible stockée dans le dépôt

## Prochaines étapes

 Déploiement complet de l’API sur AWS EC2

 Ajout d’un endpoint /health pour la supervision

 Centralisation des logs + monitoring via CloudWatch

 Mise en place de tests d’intégration live

 Ajout de tests de montée en charge (Locust)


## À propos

Projet personnel pour expérimenter  :

Infrastructure as Code (Terraform)

Conteneurisation et orchestration (Docker & Compose)

Cloud AWS (EC2, RDS, IAM, Security Groups)

Mon objectif : construire une stack complète prête pour la prod, avec CI/CD et bonnes pratiques DevOps.

