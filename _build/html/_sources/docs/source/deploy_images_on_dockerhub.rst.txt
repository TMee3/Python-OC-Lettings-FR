Déploiement images Docker, sur DockerHub
========================================

On utilisera le dépôt Docker générique: `DockerHub <https://hub.docker.com/>`_

Afin de simplifier les illustrations tout comme l'usage des commandes en local, vous aurez créer un fichier ".envrc" tel que déclaré dans `Développement local`.

Vous aurez ajouté à votre PATH courant les variables déclarées dans le fichier ".envrc".

On va exécuter un script format BASH. Sur Windows il faudra adapter, jouer les seules commandes nécessaires.

.. code-block:: console

  cd oc_projet13_orange_country_lettings/

  ./docker-compose-deployment.sh build

  ./docker-compose-deployment.sh down

  ./docker-compose-deployment.sh publish
