from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Bark


class UsersViewsTests(TestCase):
    # setUp data
    def setUp(self):
        """
        Arrange: prepare data base and URLs for the test
        """
        self.client = Client()

        self.user_registered = User.objects.create_user(
            username="user_registered_test", password="registeredtest"
        )
        self.user_visitor = User.objects.create_user(
            username="user_visitor_test", password="visitortest"
        )

        self.signup_url = reverse("signup")
        self.user_profile_url = reverse(
            "profiles", kwargs={"username": self.user_registered.username}
        )

    # signup view test
    def test_signup_redirects_registered_user(self):
        """
        Registered user is redirected their profile
        """
        self.client.login(username="user_registered_test", password="registeredtest")

        response = self.client.get(self.signup_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.user_profile_url)

    def test_signup_get_method_returns_empty_form(self):
        """
        Visitor user receives an empty form
        """
        response = self.client.get(self.signup_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/signup.html")
        self.assertIn("form", response.context)

    # profile view test
    def test_profile_requires_login(self):
        """
        Non registered user is redirected to the login page
        """
        response = self.client.get(self.user_profile_url)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(reverse("login"))

    def test_profile_visitor_view(self):
        """
        User visits other user's profiles
        """
        self.client.login(username="user_visitor_test", password="visitortest")

        response = self.client.get(self.user_profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["is_own_profile"])
        self.assertIsNone(response.context["form"])

    def test_profile_registered_user_post_bark(self):
        """
        Registered user can post barks within their profile
        """
        self.client.login(username="user_registered_test", password="registeredtest")
        post_data = {"content": "This is a test bark."}

        response = self.client.post(self.user_profile_url, data=post_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Bark.objects.filter(content="This is a test bark.").exists())

        bark = Bark.objects.get(content="This is a test bark.")
        self.assertEqual(bark.author, self.user_registered)
