from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


# Create your tests here.
class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correction_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(
            self.response, "Discpling for Development by Atomic and Irene."
        )

    def test_homepage_does_not_contain_correct_html(self):
        self.assertNotContains(self.response, "Hello there I am not on this page")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
