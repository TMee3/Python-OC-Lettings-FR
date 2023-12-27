import unittest
from unittest.mock import Mock, patch
from django.test import Client, TestCase
from django.urls import reverse
from lettings.models import Address, Letting

class TestLettingsIndexView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_with_letting(self):
        # Crée un objet Mock pour simuler la création d'une adresse et d'une location
        new_address_mock = Mock(spec=Address)
        new_letting_mock = Mock(spec=Letting)
        new_letting_mock.title = "lambda letting"

        # Utilise un contexte patch pour remplacer la méthode create de l'adresse et de la location par les mocks
        with patch.object(Address.objects, 'create', return_value=new_address_mock), \
             patch.object(Letting.objects, 'create', return_value=new_letting_mock):
            
            url = reverse("lettings_index")
            response = self.client.get(url)
            
            # Vérifie que la vue renvoie le statut 200 OK
            self.assertEqual(response.status_code, 200)
            
            # Vérifie que le bon modèle de template est utilisé
            self.assertTemplateUsed(response, 'lettings/index.html')
            
            # Vérifie que le titre de la location simulée est présent dans la réponse
            self.assertContains(response, new_letting_mock.title)

    def test_index_view_without_letting(self):
        # Utilise un contexte patch pour simuler l'absence de location
        with patch.object(Letting.objects, 'create', return_value=None):
            url = reverse("lettings_index")
            response = self.client.get(url)
            
            # Vérifie que la vue renvoie le statut 200 OK
            self.assertEqual(response.status_code, 200)
            
            # Vérifie que le bon modèle de template est utilisé
            self.assertTemplateUsed(response, 'lettings/index.html')
            
            # Vérifie qu'un message indiquant qu'aucune location n'est disponible est présent dans la réponse
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
        # Crée un objet Mock pour simuler une location
        new_letting_mock = Mock(spec=Letting)
        new_letting_mock.title = "lambda letting"
        
        # Vérifie que la représentation en chaîne de caractères de la location simulée est correcte
        self.assertEqual(str(new_letting_mock), new_letting_mock.title)

if __name__ == '__main__':
    unittest.main()
