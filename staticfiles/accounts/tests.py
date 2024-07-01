from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .views import SignupPageView


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
    def setUp(self):
        self.signup_url = reverse("signup")
        self.response = self.client.get(self.signup_url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, text="Sign Up")
        self.assertNotContains(self.response, "some random text 823k%")

    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve(self.signup_url)
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
