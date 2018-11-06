from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from django.http import Http404
from services.views import ServiceDetailView
from services.models import Service


class ServiceDetailTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def create_service(self, name="web design", slug="web-design", description="A very long description"):
        service = Service(name=name, slug=slug, description=description)
        service.save()
        
        return service

    def create_request(self, service):
        """create the request to call each instance of the view by"""
        req = self.factory.get(reverse("services:service_detail", kwargs={'slug': service.slug}))
        resp = ServiceDetailView.as_view()(req, slug=service.slug)

        return resp

    def test_service_in_context(self):
        service = self.create_service()
        resp = self.create_request(service)

        self.assertIn('service', resp.context_data)

    def test_service_is_instance_of_ServiceDetail(self):
        service = self.create_service()
        resp = self.create_request(service)
        
        self.assertTrue(isinstance(resp.context_data['service'], Service))
    
    def test_service_in_context_is_not_none_when_service_data_is_in_db(self):
        service = self.create_service()
        resp = self.create_request(service)

        self.assertIsNotNone(resp.context_data['service'], "should return Service Instance if item in service DB")
    
    def test_returns_404_errors_when_no_item_in_db(self):
        req = self.factory.get(reverse("services:service_detail", kwargs={'slug': 'web-design'}))

        with self.assertRaisesMessage(Http404, "No service found matching the query"):
            ServiceDetailView.as_view()(req, slug='web-design')

    def test_correct_template_was_used(self):
        service = self.create_service()
        resp = self.create_request(service)

        self.assertEqual(resp.template_name[0], "services/service_detail.html")