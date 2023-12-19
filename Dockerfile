# Utilisez une image de base Python
FROM python:3.8-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Créez un répertoire de travail
WORKDIR /app

# Copiez le fichier pyproject.toml et le fichier poetry.lock dans le conteneur
COPY pyproject.toml poetry.lock ./

# Installez Poetry
RUN pip install poetry

# Installez les dépendances du projet avec Poetry
RUN poetry install

# Copiez le contenu de votre projet dans le conteneur
COPY . .

