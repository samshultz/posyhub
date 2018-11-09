from django.test import TestCase
from services.admin import ServiceAdmin
from django.contrib.admin.sites import AdminSite
from django.template.defaultfilters import truncatewords
from services.models import Service

class ServiceAdminTest(TestCase):
    def test_get_brief_description(self):
        service = Service(name="web design", description=("A very long description A very "
            "long description A very long description A very long description"))
        service.save()

        site = AdminSite()
        service_admin = ServiceAdmin(Service, site)

        result = service_admin.get_brief_description(service)
        self.assertEqual(result, truncatewords(service.description, 20), "should return few characters")