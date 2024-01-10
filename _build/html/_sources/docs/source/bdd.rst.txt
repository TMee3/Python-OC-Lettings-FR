Base de données
===============

Découverte
----------

- `cd oc_projet13_orange_country_lettings/`

.. code-block:: console

  cd oc_projet13_orange_country_lettings/

  source venv/b-in/activate

- Ouvrir une session shell

.. code-block:: console

  sqlite3

- Se connecter à la base de données

.. code-block:: console

  .open oc-lettings-site.sqlite3

- Afficher les tables dans la base de données

.. code-block:: console

  .tables

- Afficher les colonnes dans le tableau des profils,

.. code-block:: console

  pragma table_info(Python-OC-Lettings-FR_profile);

- Lancer une requête sur la table des profils,

.. code-block:: console

  select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';

- quitter

.. code-block:: console

  .quit


Structure base de données
-------------------------

La structure des principales tables est la suivante. Noter que le modèle de classe User natif de Django est utilisé.

sqlite> pragma table_info(lettings_address);
  - 0|id|integer|1||1
  - 1|number|integer unsigned|1||0
  - 2|street|varchar(64)|1||0
  - 3|city|varchar(64)|1||0
  - 4|state|varchar(2)|1||0
  - 5|zip_code|integer unsigned|1||0
  - 6|country_iso_code|varchar(3)|1||0

sqlite> pragma table_info(lettings_letting);
  - 0|id|integer|1||1
  - 1|title|varchar(256)|1||0
  - 2|address_id|integer|1||0

sqlite> pragma table_info(profiles_profile);
  - 0|id|integer|1||1
  - 1|favorite_city|varchar(64)|1||0
  - 2|user_id|integer|1||0
