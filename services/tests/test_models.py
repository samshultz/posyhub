from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from services.models import Service


class ServiceModelTest(TestCase):

    @patch("services.models.Service.save", MagicMock(name="save"))
    def test_can_save_service(self):
        # img = SimpleUploadedFile(r"C:\Users\Samshultz\Pictures\Myriads\download.jpg")
        service = Service(name="web design", description="A very long description")
        service.save()
        self.assertTrue(Service.save.called) # NOQA
        self.assertEqual(Service.save.call_count, 1) # NOQA