# roav7_demo_flask

Ce projet est une petite application web construite avec **FastAPI**. Elle affiche les détails d'un produit (nom, prix, quantité en stock) et permet de réduire dynamiquement le stock en cliquant sur un bouton. Le bouton devient automatiquement grisé et désactivé lorsque le stock atteint zéro.

## Fonctionnalités
- **Affichage des détails d'un produit** : nom, prix, quantité disponible.
- **Mise à jour dynamique du stock** : chaque clic sur le bouton déduit une unité du stock.
- **Désactivation du bouton** : lorsque le stock est épuisé, le bouton est désactivé et grisé.

## Prérequis
- **Python 3.13.0** installé (peut marcher avec d'autres versions mais non testé).


## Installation et démarrage

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/superdada18/roav7_demo_flask
   cd roav7_demo_flask
   ```

2. **Installer les dépendances** :
   Créez un environnement virtuel (optionnel mais recommandé) et installez les paquets nécessaires :
   ```bash
   python -m venv env
   source env/bin/activate  # Sous Windows : .\env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Lancer l'application** :
   Exécutez le serveur FastAPI avec Uvicorn :
   ```bash
   uvicorn main:app --reload
   ```

4. **Accéder à l'application** :
   Ouvrez votre navigateur à l'adresse suivante :
   ```
   http://127.0.0.1:8000
   ```

## Structure du Projet

```
.
├── main.py                  # Code principal de l'application FastAPI
├── templates/
│   └── index.html          # Modèle HTML pour afficher les détails du produit
├── static/
│   └── style.css           # Fichier CSS pour la mise en page
├── requirements.txt        # Liste des dépendances nécessaires
└── README.md               # Documentation du projet
```


## Dépendances
- [FastAPI](https://fastapi.tiangolo.com/) : framework principal.
- [Uvicorn](https://www.uvicorn.org/) : serveur ASGI pour exécuter l'application.
- [Jinja2](https://jinja.palletsprojects.com/) : moteur de templates pour générer du HTML.

## Auteur
- **Daniel OFFNER** : Développeur de l'application.

