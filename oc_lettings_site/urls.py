import logging

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views


def demo_info_view(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Définissez le niveau de journalisation INFO explicitement
    logger.info("Ceci est un événement INFO pour Sentry")
    return HttpResponse("Événement INFO envoyé à Sentry")

def demo_error_view(request):
    logger = logging.getLogger(__name__)
    try:
        result = 1 / 0
    except Exception as e:
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
# Serve static files using Whitenoise when DEBUG is False
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()