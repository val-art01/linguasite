# Test Technique Django Multilingue avec OpenAI

Ce projet est un site Django simple et multilingue qui permet aux utilisateurs de visualiser et de créer des articles, ainsi que de poser des questions à un chatbot basé sur l’API OpenAI.

## Utilisation
Création d'un article en tent que user ou admin
Accédez à la page d'accueil pour voir les articles en ligne.
Cliquez sur "Ajouter un article".

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
git clone https://github.com/votre-utilisateur/test-technique.git
cd test-technique
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
Créez un fichier .env à la racine du projet et ajoutez-y votre clé API OpenAI.
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
Le site devrait maintenant être accessible à http://127.0.0.1:8000.

# Structure du Projet