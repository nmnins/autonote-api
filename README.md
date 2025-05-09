# 📝 AutoNote

AutoNote est une petite API REST construite avec **FastAPI**.  
Elle permet de créer, consulter et supprimer des messages techniques via des endpoints HTTP.

Ce projet m’a servi de base pour mettre en place :
- des tests unitaires avec **Pytest**
- un pipeline CI complet avec **GitHub Actions**
- une analyse automatique de style, couverture, sécurité 
- la création d'une **image Docker** fonctionnelle
- le provisionnement de base de données sur AWS via **Terraform**
- la préparation au déploiement sur **EC2 AWS**

---

![CI](https://github.com/ines835/autonote-api/actions/workflows/ci.yml/badge.svg)

---

## 🚀 Fonctionnalités

- `POST /notes` : ajouter une note
- `GET /notes` : lister toutes les notes
- `GET /notes/{id}` : récupérer une note par ID
- `DELETE /notes/{id}` : supprimer une note


🔐 Toutes les routes sont sécurisées par une **clé API** via le header `x-api-key`.


📌 Les notes sont désormais stockées dans une **base PostgreSQL hébergée sur AWS RDS**, provisionnée via Terraform.  
✅ Le passage de SQLite à PostgreSQL est complet.

---

## ⚙️ Installation locale

```bash
git clone https://github.com/ines835/autonote-api.git
cd autonote-api
python -m venv env
source env/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

📌 Si vous êtes sous Windows, exécutez `env\Scripts\activate` au lieu de `source env/bin/activate`.

---

##  Lancer les tests

```bash
pytest --cov=app --cov-report=term-missing
```

---

## Utiliser Docker 
```bash
docker build -t autonote-api .

docker run -p 8000:8000 --env-file .env autonote-api
```
## Infrastructure Terraform 

Le dossier terraform/ contient :

Provisionnement RDS PostgreSQL

Sécurité (Security Group)

Variables versionnées

## CI & sécurité

Le projet inclut un pipeline GitHub Actions qui vérifie automatiquement :

✅ la qualité du code avec ruff

✅ la couverture des tests avec pytest-cov

✅ la sécurité du code Python avec bandit

✅ les vulnérabilités des dépendances via pip-audit

✅ la validité du Dockerfile via docker build

📄 Pipeline : .github/workflows/ci.yml

---


## Structure du projet

```text
autonote-api/
├── app/                   # Code principal (routes, modèles, logique)
├── tests/                 # Tests unitaires
├── requirements.txt       # Dépendances de production
├── requirements-dev.txt   # Dépendances de développement
├── Dockerfile             # Image Docker de l'app
├── .env                   # Variables d'environnement (non versionné)
├── README.md              # ➤ Vous êtes ici :)
└── .github/
    └── workflows/
        └── ci.yml         # Pipeline CI GitHub Actions

```
--- 

## Sécurité

Les secrets ne sont pas versionnés

.env est exclu du dépôt

Un exemple .env.example est fourni

Accès PostgreSQL via Security Group limité à l’IP personnelle




## 🔜 Prochaines étapes

 Déploiement complet de l’API sur EC2 AWS

 Ajout d’une route /health pour supervision

 Monitoring (CloudWatch) et logs centralisés

 Mise en place de tests d’intégration/API live

 Ajout de tests de charge avec Locust


--- 

## À propos

Ce projet fait partie de mon apprentissage DevSecOps.
Il est conçu comme une base solide pour :

Dockerisation

CI/CD

Sécurité

Infrastructure as Code

