# 📝 AutoNote

AutoNote est une petite API REST construite avec **FastAPI**.  
Elle permet de créer, consulter et supprimer des messages techniques via des endpoints HTTP.

Ce projet m’a servi de base pour mettre en place :
- des tests unitaires avec **Pytest**
- un pipeline CI complet avec **GitHub Actions**
- une analyse automatique de style, couverture, sécurité 
- la création d'une **image Docker** fonctionnelle

---

![CI](https://github.com/ines835/autonote-api/actions/workflows/ci.yml/badge.svg)

---

## 🚀 Fonctionnalités

- `POST /notes` : ajouter une note
- `GET /notes` : lister toutes les notes
- `GET /notes/{id}` : récupérer une note par ID
- `DELETE /notes/{id}` : supprimer une note

📌 Les notes sont stockées localement dans une base **SQLite** via `SQLModel`.  
🔐 Toutes les routes sont sécurisées par une **clé API** via le header `x-api-key`.

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

docker build -t autonote-api .

docker run -p 8000:8000 --env-file .env autonote-api


## Variables d'environnement 

API_KEY=votre_clé_secrète
DATABASE_URL=sqlite:///./notes.db


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

## Limitations actuelles

Pas encore de base PostgreSQL (prévu via Terraform)

API non encore déployée (à venir sur AWS)

Pas de tests de bout en bout (API live)

Pas encore de monitoring ni de logging avancé



--- 

## À propos

Ce projet fait partie de mon apprentissage DevSecOps.
Je l'utilise comme base de travail pour expérimenter les tests, la qualité du code et l'intégration continue dans un projet Python minimal.
