from django.test import Client, TestCase
from django.urls import reverse


class TestLettingsSiteIndexView(TestCase):
    """Test cases for the Lettings Site Index view."""

    def setUp(self):
        """Set up the test environment."""
        self.client = Client()

    def test_index_view(self):
        """Test the index view of the Lettings Site."""
        # Retrieve the URL and check the response
        url = reverse("index")
        response = self.client.get(url)

        # Assert the HTTP status code, template used, and content
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
