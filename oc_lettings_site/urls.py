import logging

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from . import views

logger = logging.getLogger(__name__)


def demo_info_view(request):
    logger.info("Ceci est un événement INFO pour Sentry")
    return HttpResponse("Événement INFO envoyé à Sentry")


def demo_error_view(request):
    try:
        # Code générant une erreur
        result = 1 / 0
    except Exception as e:
        # Envoie une exception ERROR à Sentry
        logger.error("Une erreur s'est produite : %s", e)
    return HttpResponse("Événement ERROR envoyé à Sentry")


urlpatterns = [
    path("", views.index, name="index"),
    path("profiles/", include("profiles.urls")),
    path("lettings/", include("lettings.urls")),
    path("admin/", admin.site.urls),
    path("demo/info/", demo_info_view, name="demo_info"),
    path("demo/error/", demo_error_view, name="demo_error"),
]
