from django.shortcuts import get_object_or_404, render

from lettings.models import Letting


def index(request):
    """
    Displays the page containing all available lettings.

    Args:
        request (HttpRequest): The HttpRequest object.

    Returns:
        HttpResponse: An HTTP response whose content is generated based on the provided arguments.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Displays the page containing information for the selected letting.

    Args:
        request (HttpRequest): The HttpRequest object.
        letting_id (int): The ID of the selected letting.

    Returns:
        HttpResponse: An HTTP response whose content is generated based on the provided arguments.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
