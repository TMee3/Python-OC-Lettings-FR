from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """
    Represents an address.

    Attributes:
        number (int): The number of the address.
        street (str): The name of the street.
        city (str): The name of the city.
        state (str): The state code.
        zip_code (int): The ZIP code.
        country_iso_code (str): The ISO code of the country.

    Meta:
        db_table (str): The name of the database table.
        verbose_name (str): The singular name for the model.
        verbose_name_plural (str): The plural name for the model.
    """

    class Meta:
        db_table = "oc_lettings_site_address"
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Represents a letting in the Orange County Lettings site.

    Attributes:
        title (str): The title of the letting.
        address (Address): The address of the letting.

    Methods:
        __str__(): Returns a string representation of the letting.
    """

    class Meta:
        db_table = "oc_lettings_site_letting"
        verbose_name = _("Letting")
        verbose_name_plural = _("Lettings")

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
