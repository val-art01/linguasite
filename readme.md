# Test Technique Django Multilingue avec OpenAI

Ce projet est un site Django simple et multilingue qui permet aux utilisateurs de visualiser et de créer des articles, ainsi que de poser des questions à un chatbot basé sur l’API OpenAI.

## Utilisation
Création d'un article en tent que user ou admin
Accédez à la page d'accueil pour voir les articles en ligne.
Cliquez sur "Ajouter un article" pour ajouter en article en tant que utilisateur ou naviguez vers:[https://linguasite.onrender.com/admin](https://linguasite.onrender.com/admin), conctez vous avec les ID suivant: login<admin>, password<admin>.

## Utilisation du Chatbot
Accédez à la page du chatbot.
Entrez une question et soumettez le formulaire.
La réponse du chatbot sera affichée en dessous du formulaire.

## Multilingue
Pour changer la langue de l'interface utilisateur, utilisez le sélecteur de langue dans la barre de navigation. Les langues disponibles sont le français et l'anglais.

## Prérequis pour l'utilisation

Assurez-vous d'avoir installé les éléments suivants sur votre machine :
- Python 3.10+
- pip
- virtualenv

## Installation

1. Clonez le dépôt :
```sh
git https://github.com/val-art01/linguasite.git
cd linguasite
```
2. Créez un environnement virtuel et activez-le :
```sh
python -m venv env
source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
```
3. Installez les dépendances :
```shell
pip install -r requirements.txt
```
4. Configurez les variables d'environnement:
Créez un fichier .env à la racine du projet et ajoutez-y votre clé API OpenAI ainsi que l’URL de la base de données externe de Render si vous en avez une. À défaut de cela, utilisez MySQL comme base de données et configurez le fichier settings.py avec les paramètres de MySQL. Un exemple de configuration se trouve dans le fichier .env.example.
rassurez vous que votre quota actuel pour l'utilisation de l'API OpenAI n'est pas encore dépassé
```sh
    OPENAI_API_KEY=your_openai_api_key
```
5. Appliquez les migrations de la base de données:
```shell
python manage.py makemigrations
python manage.py migrate
```
6. Créez un superutilisateur pour accéder à l'admin Django :
```shell
python manage.py createsuperuser
```
7. Lancez le serveur de développement :
```shell
python manage.py runserver
```
Le site devrait maintenant être accessible en local via http://127.0.0.1:8000.

# Déploiement
Ce projet est en production sur Render via: [linguasite](https://linguasite.onrender.com/)

## Vulnérabilités de sécurité
Si vous découvrez une faille de sécurité, veuillez envoyer un courriel à Valery MAYOU via [mayoujord@gmail.cm](mayoujord@gmail.cm). 
Toutes les failles de sécurité seront traitées rapidement.

# Contribuer
Les contributions sont les bienvenues merci.