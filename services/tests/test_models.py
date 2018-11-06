from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.core.exceptions import ValidationError
from services.models import Service


class ServiceModelTest(TestCase):

    @patch("services.models.Service.save", MagicMock(name="save"))
    def test_can_save_service(self):
        service = Service(name="web design", description="A very long description")
        service.save()
        
        self.assertTrue(Service.save.called) # NOQA
        self.assertEqual(Service.save.call_count, 1) # NOQA

    
    def test_cant_save_without_name_data_provided(self):
        service = Service(description="A very long description")
        
        with self.assertRaisesMessage(ValidationError, "Name field cannot be empty"):
            service.save()
        self.assertEqual(Service.objects.count(), 0, "No Item should be created in the db")
    
    def test_slug_is_automatically_generated_on_save_if_not_present(self):
        service = Service(name="web design", description="A very long description")
        service.save()
        self.assertEqual(service.slug, 'web-design')
    
    def test_cant_save_without_description_provided(self):
        service = Service(name="web design")

        with self.assertRaisesMessage(ValidationError, "Description field cannot be empty"):
            service.save()

    def test_string_representation(self):
        service = Service(name="web design", description="A very long description")

        self.assertEqual(str(service), "web design", "should return the name of the service")

    def test_get_absolute_url_is_not_none(self):
        service = Service(name="web design", slug="web-design", description="A very long description")
        self.assertIsNotNone(service.get_absolute_url(), "should return a valid url")

    def test_get_absolute_url(self):
        service = Service(name="web design", description="A very long description")
        service.save()
        self.assertEqual(service.get_absolute_url(), "/services/web-design/")
        
        


    