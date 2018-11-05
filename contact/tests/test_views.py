from django.test import TestCase
from django.urls import reverse
from contact.forms import ContactForm
from django.test import RequestFactory
from django.core import mail

from contact.models import CompanyDetail, CompanyAddress
from contact.views import ContactView

class ContactViewTest(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()

    def get_request_using_request_factory(self):
        req = self.factory.get(reverse("contact:contact-us"))
        response = ContactView.as_view()(req)

        return response

    def test_contact_in_context(self):
        response = self.get_request_using_request_factory()
        self.assertIn('contact', response.context_data)
    
    def test_contact_is_none_if_no_item_exist_in_the_db(self):
        response = self.get_request_using_request_factory()
        self.assertIsNone(response.context_data['contact'])

    def test_form_in_context(self):
        response = self.get_request_using_request_factory()
        self.assertIn('form', response.context_data)
    
    def test_form_in_context_is_contact_form_instance(self):
        response = self.client.get(reverse("contact:contact-us"))
        self.assertTrue(isinstance(response.context['form'], ContactForm))

    def test_contact_is_a_CompanyDetail_instance_if_at_least_one_item_exist_in_the_database(self):
        company_detail = CompanyDetail.objects.create(name="Kennedy lay Ltd.",
                                                      phone_no="+234783024893", 
                                                      email="taiwogabrielsamuel@gmail.com")

        CompanyAddress.objects.create(company=company_detail, address="222, Baker street.")
        
        response = self.get_request_using_request_factory()
        self.assertTrue(isinstance(response.context_data['contact'], CompanyDetail))


    def test_contact_equals_first_element_by_pk_if_more_than_one_item_exists_in_db(self):
        """ the context variable 'contact' should return the first item
        in the DB when ordered by pk"""

        company_detail = CompanyDetail.objects.create(name="Kennedy lay Ltd.",
                                                      phone_no="+234783024893", 
                                                      email="taiwogabrielsamuel@gmail.com")
        company_detail2 = CompanyDetail.objects.create(name="RonField Ltd.",
                                                      phone_no="+2347829424893", 
                                                      email="admin@ronfield.com")

        CompanyAddress.objects.create(company=company_detail, address="222, Baker street.")
        CompanyAddress.objects.create(company=company_detail2, address="56, Kardesh Barnea")
        
        response = self.get_request_using_request_factory()
        self.assertEqual(str(company_detail), str(response.context_data['contact']))

    def test_message_sent_when_form_is_valid(self):
        req = self.factory.post(reverse('contact:contact-us'), dict(name="jon", 
                                         phone_no="+36309304993", 
                                         message="skdjkal"))
        
        ContactView.as_view()(req)
        self.assertEqual(len(mail.outbox), 1)
