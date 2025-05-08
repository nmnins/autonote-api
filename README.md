# 📝 AutoNote

AutoNote est une petite API REST construite avec FastAPI.  
Elle permet de créer, consulter et supprimer des messages textes techniques via des endpoints HTTP.

Ce projet m’a servi de base pour mettre en place :
- des tests unitaires avec Pytest
- un pipeline CI complet avec GitHub Actions
- des vérifications automatiques de style, de couverture et de sécurité 
---

![CI](https://github.com/ines835/autonote-api/actions/workflows/ci.yml/badge.svg)

---

## 🚀 Fonctionnalités actuelles

- `POST /notes` : ajouter une note
- `GET /notes` : lister toutes les notes
- `GET /notes/{id}` : récupérer une note par ID
- `DELETE /notes/{id}` : supprimer une note

📌 Les notes sont stockées temporairement dans un fichier JSON local.  
📌 Il n’y a pas encore d’authentification ni de base de données.

---

## ⚙️ Installation locale

```bash
git clone https://github.com/ines835/autonote-api.git
cd autonote-api
python -m venv venv
source venv/bin/activate
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

## CI & sécurité

Le projet inclut un pipeline GitHub Actions qui vérifie automatiquement :

✅ la qualité du code avec ruff

✅ la couverture des tests avec pytest-cov

✅ la sécurité du code Python avec bandit

✅ les vulnérabilités des dépendances via pip-audit

📁 Le fichier du pipeline se trouve dans .github/workflows/ci.yml

---

## Structure du projet

```text
autonote-api/
├── app/               # Code principal (routes, modèles)
├── tests/             # Tests unitaires
├── requirements.txt   # Dépendances de production
├── requirements-dev.txt # Dépendances de développement
├── README.md          # Vous êtes ici :)
└── .github/
    └── workflows/
        └── ci.yml     # Pipeline CI GitHub Actions
```
--- 

## Limitations actuelles

Pas encore d’authentification

Pas de base de données

Pas encore dockerisé

API non déployée

--- 

## À propos

Ce projet fait partie de mon apprentissage DevSecOps.
Je l'utilise comme base de travail pour expérimenter les tests, la qualité du code et l'intégration continue dans un projet Python minimal.
