import unittest
from unittest.mock import Mock, patch
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from profiles.models import Profile


class TestProfilesIndexView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_with_profile(self):
        # Crée un objet Mock pour simuler la création d'un utilisateur et d'un profil
        new_user_mock = Mock(spec=User)
        new_user_mock.username = "Lily"
        new_profile_mock = Mock(spec=Profile)
        new_profile_mock.user = new_user_mock
        new_profile_mock.favorite_city = "Tours"

        # Utilise un contexte patch pour remplacer la méthode create de User.objects et Profile.objects par les mocks
        with patch.object(User.objects, 'create', return_value=new_user_mock), \
             patch.object(Profile.objects, 'create', return_value=new_profile_mock):
            
            url = reverse("profiles_index")
            response = self.client.get(url)
            
            # Vérifie que la vue renvoie le statut 200 OK
            self.assertEqual(response.status_code, 200)
            
            # Vérifie que le bon modèle de template est utilisé
            self.assertTemplateUsed(response, 'profiles/index.html')
            
            # Vérifie que le nom d'utilisateur simulé est présent dans la réponse
            self.assertContains(response, new_user_mock.username)

    def test_index_view_without_profile(self):
        # Utilise un contexte patch pour simuler l'absence de profil
        with patch.object(Profile.objects, 'create', return_value=None):
            url = reverse("profiles_index")
            response = self.client.get(url)
            
            # Vérifie que la vue renvoie le statut 200 OK
            self.assertEqual(response.status_code, 200)
            
            # Vérifie que le bon modèle de template est utilisé
            self.assertTemplateUsed(response, 'profiles/index.html')
            
            # Vérifie qu'un message indiquant qu'aucun profil n'est disponible est présent dans la réponse
            self.assertContains(response, 'No profiles are available')


class TestProfilesProfileView(TestCase):
    def setUp(self):
        self.client = Client()
        self.new_user = User.objects.create(username="Lily")
        self.new_profile = Profile.objects.create(user=self.new_user, favorite_city="Tours")

    def test_profile_view_with_profile(self):
        url = reverse("profile", args=[self.new_user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, self.new_user.username)

    def test_profile_view_with_unknown_profile(self):
        url = reverse("profile", args=["Joost"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')


class TestProfilesModels(TestCase):
    def test_profile_model_str(self):
        # Crée un objet Mock pour simuler un utilisateur
        new_user_mock = Mock(spec=User)
        new_user_mock.username = "Lily"

        # Crée un objet Mock pour simuler un profil associé à l'utilisateur
        new_profile_mock = Mock(spec=Profile)
        new_profile_mock.user = new_user_mock

        # Vérifie que la représentation en chaîne de caractères du profil simulé est correcte
        self.assertEqual(str(new_profile_mock), new_user_mock.username)


if __name__ == '__main__':
    unittest.main()
