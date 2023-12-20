from django.contrib import admin
from django.urls import path

from lettings import views as lettings_views
from profiles import views as profiles_views
from oc_lettings_site import views as oc_lettings_site_views

import logging
from django.http import HttpResponse

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
    path("", oc_lettings_site_views.index, name="index"),
    path("lettings/", lettings_views.lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", lettings_views.letting, name="letting"),
    path("profiles/", profiles_views.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", profiles_views.profile, name="profile"),
    path("admin/", admin.site.urls),
    path('demo/info/', demo_info_view, name='demo_info'),
    path('demo/error/', demo_error_view, name='demo_error'),
]
