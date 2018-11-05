from django.test import TestCase, RequestFactory
from about.views import DisplayAboutView
from django.urls import reverse
from about.models import AboutCompany


class DisplayAboutViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def get_request_factory_response(self):
        req = self.factory.get(reverse("about:about-us"))
        response = DisplayAboutView.as_view()(req)

        return response

    def test_correct_template_was_used(self):
        response = self.get_request_factory_response()
        
        self.assertEqual(response.template_name[0], 'about/about.html')

    def test_about_in_context(self):
        response = self.get_request_factory_response()

        self.assertIn('about', response.context_data)

    def test_about_is_an_instance_of_about_company_if_at_least_one_item_in_db(self):
        addr = AboutCompany(content="Hello to you")
        addr.save()
        response = self.get_request_factory_response()
        
        self.assertTrue(isinstance(response.context_data['about'], AboutCompany))
