# Euphoria
A Django based Personal Resume website project. Designed to
comply with the specifications of ```#track-backend``` level: ```stage 2``` of [Zuri Internship](). View the project here

## Features
* Fully functional contact submission form.
* Dynamic website data

## Setting up this project locally
This project requires Python-3.9.5 and pipenv for project dependency and project virtual environment. To install pipenv ```pip install pipenv```
1. Clone this repository
2. Enter project directory ```cd euphoria```
3. Install project dependencies and project virtual environment ```pipenv install```
4. Set ```DEBUG=False``` in the ```settings.py``` file located in the euphoria subfolder which also holds the  ```wsgi.py``` file.
5. Export the projects enviromental variables. Note: only the ```DJANGO_SECRET_KEY``` env var is required to get the project running once ```python DEBUG=False``` in the ```settings.py``` file.
You can find out about other env vars in [Environmental Variables](##Enviromental-Variables)
6. From the project's root directory in your cmd or terminal run ```python manage.py migrage``` to setup your local env database and ```python manager.py runserver``` to start the development server.
7. Visit the project from your preferred web browser via [http://localhost:8000](http://localhost:8000)

## Environmental Variables
- DJANGO_SECRET_KEY
- D_DATABASE
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_STORAGE_BUCKET_NAME