Mettre à jour les variables d'environnement
===========================================

On met à jour le PATH pour la seule exécution en locale.

.. code-block:: console

  cd oc_projet13_orange_country_lettings/

Créer un fichier ".envrc" avec les variables suivantes (à adapter avec vos identifiants):

Contenu fichier .envrc
  export BETTERSTACK_SOURCE_TOKEN='SuperTokenFromBetterStack'

  export COVERALLS_REPO_TOKEN=SuperTokenFromCoveralls

  export SECRET_KEY='MakeYourOwnSecretKey'

  export DJANGO_ALLOWED_HOSTS='localhost,127.0.0.1'

  export DEBUG=0

  export DOCKER_HUB_USER='YourDockerHubUser'

  export DOCKER_HUB_PASSWORD='YourDockerHubPassword'

NB: les 2 exports DOCKER_HUB_* sont optionnels. Nécessaires que pour publier ses propres images locales vers un dépôt Docker. Voir section 'Déploiement'.

Ajouter les variables au PATH courant:

.. code-block:: console

  source .envrc

Noter que le logger est déclaré dans le fichier "logtail_handler.py".
