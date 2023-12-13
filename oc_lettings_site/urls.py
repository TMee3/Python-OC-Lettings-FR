from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", views.lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),
    path("profiles/", views.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", views.profile, name="profile"),
    path("admin/", admin.site.urls),
]

"""
URL patterns for the Orange County Lettings site.

- The root URL ("/") maps to the index view.
- The "/lettings/" URL maps to the lettings_index view.
- The "/lettings/<int:letting_id>/" URL maps to the letting view, which displays details of a specific letting.
- The "/profiles/" URL maps to the profiles_index view.
- The "/profiles/<str:username>/" URL maps to the profile view, which displays details of a specific user profile.
- The "/admin/" URL maps to the Django admin site.
"""
