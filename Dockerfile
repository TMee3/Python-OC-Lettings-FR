# Utilisez une image de base Python
FROM python:3.11

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Créez un répertoire de travail
WORKDIR /project

# Installation de Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copiez le fichier pyproject.toml et le fichier poetry.lock dans le conteneur
COPY pyproject.toml poetry.lock ./

# Installez les dépendances du projet avec Poetry
RUN poetry install --no-dev

# Copiez le contenu de votre projet dans le conteneur
COPY . .

EXPOSE 8000 
# Exécutez le serveur de développement
CMD poetry run python manage.py runserver 0.0.0.0:8000