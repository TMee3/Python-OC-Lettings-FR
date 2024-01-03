from django.test import Client, TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class TestLettingsIndexView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_with_letting(self):
        new_address = Address.objects.create(
            number=1,
            street="Lambda Street",
            city="Nowhere",
            state="GA",
            zip_code=31525,
            country_iso_code="USA"
        )
        new_letting = Letting.objects.create(address=new_address, title="lambda letting")
        url = reverse("lettings_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, new_letting.title)

    def test_index_view_without_letting(self):
        url = reverse("lettings_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, 'No lettings are available')


class TestLettingsLettingView(TestCase):
    def setUp(self):
        self.client = Client()
        self.new_address = Address.objects.create(
            number=1,
            street="Lambda Street",
            city="Nowhere",
            state="GA",
            zip_code=31525,
            country_iso_code="USA"
        )
        self.new_letting = Letting.objects.create(address=self.new_address, title="lambda letting")

    def test_letting_view_with_letting(self):
        url = reverse("letting", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, self.new_letting.title)

    def test_letting_view_with_unknown_letting(self):
        url = reverse("letting", args=[555])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')


class TestLettingsModels(TestCase):
    def setUp(self):
        self.new_address = Address.objects.create(
            number=1,
            street="Lambda Street",
            city="Nowhere",
            state="GA",
            zip_code=31525,
            country_iso_code="USA"
        )

    def test_address_model_str(self):
        self.assertEqual(str(self.new_address),
                         f"{self.new_address.number} {self.new_address.street}")

    def test_letting_model_str(self):
        new_letting = Letting.objects.create(address=self.new_address, title="lambda letting")
        self.assertEqual(str(new_letting), new_letting.title)
