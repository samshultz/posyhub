from django.test import TestCase
from contact.forms import ContactForm
from django.core import mail


class ContactFormTest(TestCase):

    def test_form_with_invalid_data(self):
        form = ContactForm(dict(name="jon", phone_no="", message="skdjkal"))
        self.assertFalse(form.is_valid())
    
    def test_form_with_valid_data(self):
        form = ContactForm(dict(name="jon", phone_no="+36309304993", message="skdjkal"))
        self.assertTrue(form.is_valid())

    def test_can_send_mail_with_valid_data(self):
        form = ContactForm(dict(name="jon", phone_no="+36309304993", message="skdjkal"))
        form.send_email(dict(name="jon", phone_no="+36309304993", message="skdjkal"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "A new message from jon a potential client")