
from django.shortcuts import render
from profiles.models import Profile

def profiles_index(request):
    """Profiles index view, list all profiles"""

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/profiles_index.html", context)


def profile(request, username):
    """
    Profile view, show a profile details

    params: username (str)
    """

    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)

