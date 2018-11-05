from django.test import TestCase
from django.urls import resolve, reverse
from about.views import DisplayAboutView


class AboutUrlTest(TestCase):

    def test_correct_view_was_used(self):
        found = resolve(reverse("about:about-us"))
        self.assertEqual(found.func.__name__, DisplayAboutView.as_view().__name__)