from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from profiles.models import Profile


class TestProfilesIndexView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_with_profile(self):
        new_user = User.objects.create(username="Lily")
        Profile.objects.create(user=new_user, favorite_city="Tours")
        url = reverse("profiles_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, new_user.username)

    def test_index_view_without_profile(self):
        url = reverse("profiles_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, 'No profiles are available')


class TestProfilesProfileView(TestCase):
    def setUp(self):
        self.client = Client()
        self.new_user = User.objects.create(username="Lily")
        Profile.objects.create(user=self.new_user, favorite_city="Tours")

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
    def test_address_model_str(self):
        new_user = User.objects.create(username="Lily")
        new_profile = Profile.objects.create(user=new_user, favorite_city="Tours")
        self.assertEqual(str(new_profile), new_user.username)
