from django.test import TestCase
from django.urls import resolve, reverse

from .views import HomePageView


class HomePageTests(TestCase):
    def setUp(self):
        pass

    def test_home_page_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("home.html")

    def test_home_page_name(self):
        response = self.client.get(reverse(viewname="pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("home.html")
        self.assertContains(response, text="home")
        self.assertNotContains(response, text="some random text 38@£@8")

    def test_homepage_url_resolves_correct_view(self):
        view_name = resolve(path="/").func.__name__
        self.assertEqual(view_name, HomePageView.as_view().__name__)
