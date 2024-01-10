Exécuter le site, en local, avec Docker
=======================================

Vous devez avoir installé "docker" (ou podman) et "docker-compose".

On va exécuter un script format BASH. Sur Windows il faudra adapter, jouer les seules commandes nécessaires.

.. code-block:: console

  cd oc_projet13_orange_country_lettings/

Pour une première exécution:

.. code-block:: console

  ./docker-compose-deployment.sh build

Dans le cas où vous avez déjà les images en local et l'application initialisée:

.. code-block:: console

  ./docker-compose-deployment.sh run

Pour arrêter les conteneurs:

.. code-block:: console

  ./docker-compose-deployment.sh down

Remarque: noter que vous pouvez télécharger les 2 images publiques suivantes (usage de podman ou docker selon les versions d'OS):

.. code-block:: console

  podman pull docker.io/memphistools/public_repo:oc_projet13_orange_country_lettings_web

  podman pull docker.io/memphistools/public_repo:oc_projet13_orange_country_lettings_nginx
