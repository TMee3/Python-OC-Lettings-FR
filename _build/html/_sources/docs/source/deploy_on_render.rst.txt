Déploiement application en ligne
================================

Le choix a été fait de déployer sous forme d'application le projet, sur la plateforme `Render: <https://render.com/>`_.

**Tout commit de la seule branche "master"** aura pour effet de redéployer l'application.

Pour information, seul Render fait l'appel de commande suivant pour le build du projet (vous n'aurez pas l'usage de l'argument pour du dev local):

- `./docker-compose-deployment.sh cloud`

Par le biais d'un webhook exécuté depuis le pipeline en dernière étape, l'application est re-publiée sur Render.
