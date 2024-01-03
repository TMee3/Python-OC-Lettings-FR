from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """A class to represent an address.

    Attributes:
        number (int): Number where is the letting
        street (str): Street where is the letting
        city (str): City where is the letting
        state (str): State where is  the letting like GA for Georgia
        zip_code (int): Zipcode where is the letting
        country_iso_code (str): Country ISO code where is the letting like USA

    Methods:
        __str__: display number and street when str() is called
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        # avoids bad pluralization
        verbose_name_plural = "Address"

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """A class to represent a letting.

    Attributes:
        title (str): Title of the letting
        address (obj): Address linked to the letting

    Methods:
        __str__: display title of the letting when str() is called
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
