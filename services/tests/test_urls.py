from django.test import TestCase
from django.urls import resolve, reverse
from services.views import ServiceDetailView, ServiceListView
from services.models import Service


class ServiceUrlsTests(TestCase):

    def test_detail_url_calls_correct_view(self):
        service = Service(name="web design", slug="web-design", description="A very long description")
        service.save()

        found = resolve(service.get_absolute_url())
        self.assertEqual(found.func.__name__, ServiceDetailView.as_view().__name__)

    def test_list_view_url_calls_correct_view(self):
        found = resolve(reverse("services:services_list"))
        self.assertEqual(found.func.__name__, ServiceListView.as_view().__name__)
