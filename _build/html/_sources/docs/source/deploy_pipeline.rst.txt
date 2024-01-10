Construction d'un pipeline de test, de build et de publication
==============================================================

En tant que développeur vous travaillerez à partir du dépôt clôné.

Pour vérifier et/ou publier les actions effectuées une automatisation est mise en place via `Circleci <https://circleci.com/>`_

Il s'agit d'un processus qui va réaliser des actions déclarées dans un fichier et format préconvenu: .circleci/config.yml.

Les actions consistent à effectuer les tests à la place du développeur, à contrôler le "lint", à effectuer le build et publication des images Docker.

Toute mise à jour de branche autre que master provoque génération d'un pipeline sans build:

- test, lint.

Toute mise à jour de branche development provoque le build (mise à jour image sur DockerHub):

- test, lint, build

**Toute mise à jour de la seule branche master provoque génération d'un pipeline avec republication de l'application en ligne**:

- test, lint, build (avec mise à jour image sur DockerHub). et publish redéploiement de l'application sur Render.
