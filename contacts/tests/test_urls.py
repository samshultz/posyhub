from django.test import TestCase
from django.urls import reverse, resolve
from contact.views import ContactView


class TestContactUrls(TestCase):
    def test_url_calls_correct_view(self):
        found = resolve(reverse("contact:contact-us"))

        self.assertEqual(found.func.__name__, ContactView.as_view().__name__)
        