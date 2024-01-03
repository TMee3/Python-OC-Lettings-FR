from django.test import Client, TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsTestCase(TestCase):
    """Base TestCase for Lettings app."""

    def setUp(self):
        """Set up the test environment."""
        self.client = Client()
        self.address = Address.objects.create(
            number=1,
            street="Lambda Street",
            city="Nowhere",
            state="GA",
            zip_code=31525,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            address=self.address, title="Lambda Letting"
        )


class TestLettingsIndexView(LettingsTestCase):
    """Test cases for the Lettings Index view."""

    def test_index_view_with_existing_letting(self):
        """Test displaying the list of lettings with an existing letting."""
        url = reverse("lettings_index")
        response = self.client.get(url)

        # Assertions for HTTP response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, self.letting.title)

    def test_index_view_without_letting(self):
        """Test displaying the list of lettings without any letting."""
        Letting.objects.all().delete()  # Delete all lettings
        url = reverse("lettings_index")
        response = self.client.get(url)

        # Assertions for HTTP response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, "No lettings are available")


class TestLettingsLettingView(LettingsTestCase):
    """Test cases for the Lettings Letting view."""

    def test_letting_view_with_existing_letting(self):
        """Test displaying details of an existing letting."""
        url = reverse("letting", args=[self.letting.id])
        response = self.client.get(url)

        # Assertions for HTTP response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertContains(response, self.letting.title)

    def test_letting_view_with_unknown_letting(self):
        """Test displaying details of an unknown letting."""
        url = reverse("letting", args=[555])
        response = self.client.get(url)

        # Assertions for HTTP response
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")


class TestLettingsModels(LettingsTestCase):
    """Test cases for the Lettings models."""

    def test_address_model_str(self):
        """Test the string representation of the Address model."""
        self.assertEqual(
            str(self.address), f"{self.address.number} {self.address.street}"
        )

    def test_letting_model_str(self):
        """Test the string representation of the Letting model."""
        self.assertEqual(str(self.letting), self.letting.title)
