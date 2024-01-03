from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """A class to represent a user profile.

    Attributes:
        user (obj): The User object linked to the profile.
        favorite_city (str): The user's favorite city.

    Methods:
        __str__: Returns the username of the user when str() is called.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
