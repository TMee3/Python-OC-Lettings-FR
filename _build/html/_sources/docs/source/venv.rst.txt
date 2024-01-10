Créer l'environnement virtuel
=============================

.. code-block:: console

  cd /path/to/Python-OC-Lettings-FR

  python -m venv venv

  apt-get install python3-venv`

Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu

- Activer l'environnement

.. code-block:: console

  source venv/bin/activate

- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel: `which python`

.. code-block:: console

  python

  which python

- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure:

.. code-block:: console

  python --version

- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`

.. code-block:: console

  pip

  which pip

- Pour désactiver l'environnement:

.. code-block:: console

  deactivate
