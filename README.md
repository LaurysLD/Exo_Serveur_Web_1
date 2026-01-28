# Exo_Serveur_Web_1

Serveur web Flask pédagogique avec navigation par boutons (formulaires), inscription/connexion,
et gestion d'éléments en mémoire (CRUD).

## Prérequis
- Python 3.9+
- `pip`

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install flask
```

## Lancer le serveur
```bash
python serverWEB.py
```

Puis ouvrir http://127.0.0.1:5000/ dans un navigateur.

## Fonctionnalités
- Navigation uniquement via boutons HTML (formulaires GET/POST)
- Inscription / Connexion (authentification simple)
- Création / Modification / Suppression d'éléments
- Données stockées uniquement en mémoire (perdues à l'arrêt)

## Routes principales
- `/` : accueil
- `/register` : inscription
- `/login` : connexion
- `/items` : liste + création d'éléments (protégée)
