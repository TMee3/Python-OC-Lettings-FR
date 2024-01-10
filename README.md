- [Résumé](#résumé)
- [Développement local](#développement-local)
  - [Prérequis](#prérequis)
  - [macOS / Linux](#macos--linux)
    - [Cloner le repository](#cloner-le-repository)
    - [Créer l'environnement virtuel](#créer-lenvironnement-virtuel)
    - [Exécuter le site](#exécuter-le-site)
    - [Linting](#linting)
    - [Tests unitaires](#tests-unitaires)
    - [Base de données](#base-de-données)
    - [Panel d'administration](#panel-dadministration)
  - [Windows](#windows)
- [Tests et déploiement via CircleCI](#tests-et-déploiement-via-circleci)
  - [Prérequis](#prérequis-1)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
- [Exécution du docker en local](#exécution-du-docker-en-local)
  - [Prérequis](#prérequis-2)
  - [Utilisation](#utilisation-1)
- [Sentry](#sentry)
  - [Prérequis](#prérequis-3)
  - [Utilisation](#utilisation-2)
- [Variables d'environnement](#variables-denvironnement)
  
## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis


Résumé des prérequis pour le développement local :

Vous devez disposer d'un compte GitHub avec des autorisations de lecture pour accéder à ce référentiel.
Vous devez avoir Git CLI installé.
Vous devez avoir SQLite3 CLI installé.
Vous devez avoir un interpréteur Python, version 3.6 ou ultérieure, configuré de manière à ce que la commande python dans votre shell OS exécute l'interpréteur Python requis, sauf si un environnement virtuel est activé.

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/TMee3/Python-OC-Lettings-FR.git

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `poetry install` 



#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `poetry shell`
- `poetry instal`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `poetry shell`
- `flake8 .`
- `black .`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `poetry shell`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, - `poetry shell`


## Tests et déploiement via CircleCI


Après une mise à jour du code sur la branche master, CircleCI déclenche un pipeline qui suit les étapes suivantes :

Linting du code : Le code est analysé pour détecter et corriger les erreurs de style et de formatage conformément aux conventions définies.

Exécution des tests unitaires : Les tests unitaires sont exécutés pour s'assurer que les différentes parties de l'application fonctionnent correctement de manière isolée.

Dockerisation de l'application : Une fois les tests réussis, l'application est encapsulée dans un conteneur Docker, ce qui permet de créer un environnement d'exécution cohérent et portable.

Publication de l'image Docker : L'image Docker est ensuite marquée (taguée) avec une version spécifique et téléchargée vers DockerHub, un registre de conteneurs en ligne.

Déploiement sur Render : Enfin, si toutes les étapes précédentes ont été achevées avec succès, l'application est automatiquement déployée sur la plateforme Render, rendant ainsi la dernière version du code accessible en ligne.

Ce processus garantit une intégration continue (CI) et un déploiement continu (CD) pour assurer que le code mis à jour est testé, conteneurisé et déployé de manière fiable et automatisée.

### Prérequis

Il est nécessaire de créer les comptes suivants :

- Compte [CircleCI](https://circleci.com/signup/)
- Compte [DockerHub](https://hub.docker.com/)
- Compte [RENDER](https://render.com/)


### Installation

- Créer un projet CircleCI et le lier à votre repository GitHub.
- Créer un projet DockerHub.
- Créer un projet Render.
- Obtenir le deploy hook [Documentation](https://docs.render.com/deploy-hooks#:~:text=Deploy%20hooks%20enable%20you%20to,with%20a%20single%20HTTP%20request.&text=Your%20deploy%20hook%20URL%20is,it%20by%20clicking%20Regenerate%20Hook.). (le lien sera à renseigner comme variable dans CircleCi)
  

### Utilisation

- Si toute l'installation est respectée, l'exécution du pipeline devrait se lancer à chaque mise à jour du code sur GitHub.
- Les tests unitaires et le lint du code se fera à chaque mise à jour de code dans n'importe quelle branche contenant la configuration CircleCI.
- La dockerization sur DockerHub et le déploiement sur Heroku s'exécuteront à chaque mise à jour du code dans la branche master.
 
Après le déploiement le site est accéssible à l'adresse: [python-oc-lettings-fr.onrender.com](https://python-oc-lettings-fr.onrender.com/)

## Exécution du docker en local

### Prérequis

- Compte [DockerHub](https://hub.docker.com/)
- Installer Docker
  - Linux Ubuntu : [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
  - Windows : [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)
- Avoir exécuté le Pipeline précédent (sur CircleCi).


### Utilisation

En considérant:
- user = Nom d'utilisateur du compte DockerHub.
- repo = Application créée dans DockerHub.
- tag = Nom donné automatiquement à une image.
- port = port bind 

Etapes:
- Ouvrir un terminal avec les privilèges "root".
  - Télécharger l'image docker `docker pull user/repo:tag`.
  - Exécuter l'image docker `docker run -d -e "PORT=port" -p 8000:8000 user/repo:tag`. (si vous lancez uniquement cette commande, l'image Docker sera aussi télégargée)


Exemple : docker run -p 8000:8000 tmee3/p13:1.0

Pour accéder au site rendez-vous à l'adresse: [localhost:8000](http://localhost:8000)


## Sentry

Sentry est une application de suivi d'exceptions non gérées.

### Prérequis

- Compte [Sentry](https://sentry.io/signup/)

### Utilisation

- Créer un projet Sentry

## Variables d'environnement

Les variables d'environnement sont des données sensibles à ne pas publier.

Pour se faire ces variables seront rajoutées dans :
- la configuration du projet dans CircleCI


| Clé  | Valeur          | Lieu |
| :--------------: |:---------------:|:---------:|
| DOCKERHUB_USERNAME  | Utilisateur DockerHub  | CircleCI |
| DOCKERHUB_PASSWORD	  | Mot de passe DockerHub  | CircleCI |
| RENDER_WEBHOOK		  | Lien du web hook | CircleCI |
| CIRCLE_BUILD_NUM			  | Version du build docker | CircleCI |


### DOCS Read the docs
Pour acceder à la doc aller sur :  [Read the docs](https://python-oc-lettings-docs.readthedocs.io/en/latest/instructions_installation.html/) 

### Coverage 
Pour acceder au coverage aller sur htmlcov/index.html du git.