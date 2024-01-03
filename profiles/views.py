from django.shortcuts import get_object_or_404, render

from profiles.models import Profile


def index(request):
    """
    View for displaying a page with all profiles.

    This view retrieves all profiles from the database and renders them in the 'profiles/index.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: An HTTP response containing the rendered template with the profiles list.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    View for displaying a page containing information for the selected profile.

    This view retrieves the profile associated with the given username from the database and renders it
    in the 'profiles/profile.html' template.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the selected profile.

    Returns:
        HttpResponse: An HTTP response containing the rendered template with the selected profile's information.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
