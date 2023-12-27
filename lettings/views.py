from django.shortcuts import render, get_object_or_404

from lettings.models import Letting
from django.shortcuts import render


def index(request):
    """Home page, index view"""

    return render(request, "index.html")


def lettings_index(request):
    """Lettings index view, list all lettings"""

    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/lettings_index.html", context)


def letting(request, letting_id):
    """
    Letting view, show a letting details

    params: letting_id (int)
    """

    letting = get_object_or_404(Letting, pk=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)

