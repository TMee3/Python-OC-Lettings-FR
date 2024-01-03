from django.test import Client, TestCase
from django.urls import reverse


class TestLettingsSiteIndexView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, "Welcome to Holiday Homes")
