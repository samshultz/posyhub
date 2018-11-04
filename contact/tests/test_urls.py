from django.test import TestCase
from django.urls import reverse
from contact.views import ContactView


class TestContactUrls(TestCase):
    def test_url_calls_correct_view(self):
        response = self.client.get(reverse("contact:contact-us"))
        self.assertEqual(response.resolver_match.func.__name__, ContactView.as_view().__name__)
        