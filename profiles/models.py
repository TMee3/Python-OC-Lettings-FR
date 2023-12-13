from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (User): The associated user for this profile.
        favorite_city (str): The favorite city of the user.
    """

    class Meta:
        db_table = "oc_lettings_site_profile"
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
