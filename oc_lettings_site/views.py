from django.shortcuts import render

from lettings.models import Letting
from profiles.models import Profile


def index(request):
    """Home page, index view"""

    return render(request, "index.html")


def lettings_index(request):
    """
    View function for displaying the lettings index page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered lettings index page.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/lettings_index.html", context)


def letting(request, letting_id):
    """
    View function for displaying a single letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to be displayed.

    Returns:
        HttpResponse: The HTTP response object containing the rendered letting template.
    """

    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)


def profiles_index(request):
    """
    View function to display the index page for profiles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered HTML page.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/profiles_index.html", context)


def profile(request, username):
    """
    View function to display the profile of a user.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user.

    Returns:
        HttpResponse: The HTTP response object containing the rendered profile template.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
