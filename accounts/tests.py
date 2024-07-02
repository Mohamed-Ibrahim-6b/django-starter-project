from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserTests(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpassword",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = self.User.objects.create_superuser(
            username="testuser",
            email="testuser@email.com",
            password="testpassword",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@email.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, second=200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, text="Sign Up")
        self.assertNotContains(self.response, text="some random text 92834")

    def test_signup_form(self):
        user_manager = get_user_model().objects
        user = user_manager.create_user(self.username, self.email)
        self.assertEqual(user_manager.all().count(), 1)
        self.assertEqual(user_manager.all()[0].username, self.username)
        self.assertEqual(user_manager.all()[0].email, self.email)
