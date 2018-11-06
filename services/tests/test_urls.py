from django.test import TestCase
from django.urls import resolve
from services.views import ServiceDetailView
from services.models import Service


class ServiceUrlsTests(TestCase):

    def test_detail_url_calls_correct_view(self):
        service = Service(name="web design", slug="web-design", description="A very long description")
        service.save()

        found = resolve(service.get_absolute_url())
        self.assertEqual(found.func.__name__, ServiceDetailView.as_view().__name__)
