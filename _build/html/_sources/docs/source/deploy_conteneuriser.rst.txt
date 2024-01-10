Conteneurisation de l'application
=================================

L'arborescence du projet est adaptée à une conteneurisation basique de Docker, "dans un contexte similaire à celui présenté"".

2 services supplémentaires sont introduits: Gunicorn et Nginx.

Gunicorn va servir le contenu délivré par l'application Python (Django en l'occurence). Gunicorn et le code applicatif formeront 1 service global.

Nginx servira de reverse proxy 'au service' de Gunicorn, en servant tout fichier statique: images, css, js etc.

On aura 2 conteneurs Docker, 1 pour chaque service. Ils sont orchestrés par "docker-compose (Compose)": on ne lance pas l'un sans l'autre.

Un fichier "docker-compose.dev.yml" est celui utilisé lors des phases de "build"

Un second fichier "docker-compose.prod.yml" est celui utilisé lors des phsases "d'exécution".

Un script unique permet de déployer l'application sur Docker, soit localement, soit sur cloud: docker-compose-deployment.sh.
