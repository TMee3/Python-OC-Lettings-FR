Exécuter le site, en local, sans Docker
=======================================

.. code-block:: console

  cd oc_projet13_orange_country_lettings/

  source venv/bin/activate

  pip install --requirement ./oc_projet13/requirements.txt

  python manage.py runserver

- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
