from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from profiles.models import Profile


class TestProfilesIndexView(TestCase):
    """Test cases for the Profiles Index view."""

    def setUp(self):
        """Set up the test environment."""
        self.client = Client()
        self.user = User.objects.create(username="Alice")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_index_view_with_profile(self):
        """Test the index view with a profile."""
        url = reverse("profiles_index")
        response = self.client.get(url)

        # Assertions for HTTP response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertContains(response, self.user.username)

    def test_index_view_without_profile(self):
        """Test the index view without a profile."""
        self.profile.delete()  # Delete the profile
        url = reverse("profiles_index")
        response = self.client.get(url)

        # Assertions for HTTP response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertContains(response, "No profiles are available")


class TestProfilesProfileView(TestCase):
    """Test cases for the Profiles Profile view."""

    def setUp(self):
        """Set up the test environment."""
        self.client = Client()
        self.user = User.objects.create(username="Bob")
        self.profile = Profile.objects.create(user=self.user, favorite_city="London")

    def test_profile_view_with_profile(self):
        """Test the profile view with a profile."""
        url = reverse("profile", args=[self.user.username])
        response = self.client.get(url)

        # Assertions for HTTP response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertContains(response, self.user.username)

    def test_profile_view_with_unknown_profile(self):
        """Test the profile view with an unknown profile."""
        url = reverse("profile", args=["Eve"])
        response = self.client.get(url)

        # Assertions for HTTP response
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")


class TestProfilesModels(TestCase):
    """Test cases for the Profiles model."""

    def test_profile_model_str(self):
        """Test the string representation of the Profile model."""
        user = User.objects.create(username="Charlie")
        profile = Profile.objects.create(user=user, favorite_city="Berlin")

        # Check the string representation
        self.assertEqual(str(profile), user.username)
