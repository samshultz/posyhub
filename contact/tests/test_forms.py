from django.test import TestCase
from contact.forms import ContactForm


class ContactFormTest(TestCase):

    def test_form_with_invalid_data(self):
        form = ContactForm(dict(name="jon", phone_no="", message="skdjkal"))
        self.assertFalse(form.is_valid())
    
    def test_form_with_valid_data(self):
        form = ContactForm(dict(name="jon", phone_no="+36309304993", message="skdjkal"))
        self.assertTrue(form.is_valid())
