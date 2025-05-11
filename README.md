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

### Déploiement cloud (EC2 + RDS)
L’infrastructure est provisionnée automatiquement avec Terraform :
- Une base de données PostgreSQL RDS
- Une instance EC2 Ubuntu avec Docker installé
- Des security groups configurés

Le script user_data.sh provisionne tout sauf le fichier .env.
Lancement de l’API : une étape manuelle est nécessaire après le déploiement.

### Étapes post-déploiement 

•	Se connecter à l’instance EC2 

   ssh -i ma-cle.pem ubuntu@<IP_PUBLIQUE_EC2>

•	 Aller dans le dossier du projet 

```bash
   cd autonote-api
```
•	Créer le fichier .env avec les informations postgresql RDS 

   ```bash
   cp copy .env.example .env 
   nano .env
```
•	Renseigner les champs 

   API_KEY=ton_api_key
   DATABASE_URL=postgresql://user:password@<rds-endpoint>:5432/nom_de_la_db

•	Puis lancer la commande

```bash
   docker compose up -d
```
 L’API est ensuite disponible à l’adresse :

http://<IP_PUBLIQUE_EC2>:8000

### Installation locale

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
###  Lancer les tests
   ```bash

pytest --cov=app --cov-report=term-missing
```

### Utilisation avec Docker
   ```bash

docker compose up –build
```

### Infrastructure AWS via Terraform

Le dossier terraform/ contient :
- Provisionnement automatique d'une instance RDS PostgreSQL
- Provisionnement d’une instance EC2 Ubuntu avec Docker
- Configuration des security groups

### CI & Sécurité

Le pipeline GitHub Actions vérifie à chaque push :
- Style et erreurs avec ruff
- Couverture des tests avec pytest-cov
- Vulnérabilités avec bandit et pip-audit
- Validité du Dockerfile avec docker build

📄 Pipeline : .github/workflows/ci.yml

### Structure du projet

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

### Sécurité

- Secrets gérés localement via .env
- Accès à PostgreSQL RDS restreint à l’IP personnelle et à l’EC2
- Aucune donnée sensible stockée dans le dépôt

### Prochaines étapes

- [ ] Automatiser la génération du fichier .env via Terraform (templatefile)
- [ ] Centralisation des logs + monitoring via CloudWatch
- [ ] Mise en place de tests d’intégration live
- [ ] Tests de montée en charge avec Locust

### À propos

Projet personnel pour expérimenter :
- Infrastructure as Code (Terraform)
- Conteneurisation (Docker & Compose)
- Déploiement cloud (EC2, RDS, IAM, Security Groups)
- CI/CD avec GitHub Actions

🎯 Objectif : construire une stack simple mais complète prête pour la production, avec bonnes pratiques DevOps.

