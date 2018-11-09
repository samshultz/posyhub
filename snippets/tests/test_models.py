from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.core.exceptions import ValidationError

from snippets.models import NewSocialMediaLink, SocialMediaLinks, SupportEmail, SupportEmails


class SupportEmailsTest(TestCase):

    def test_string_representation(self):
        emails = SupportEmails()
        self.assertEqual(str(emails), 'Support Emails')

    @patch("snippets.models.SupportEmails.save", MagicMock(name="save"))
    def test_can_create_social_media_link(self):
        email = SupportEmails()
        email.save()

        self.assertTrue(SupportEmails.save.called) #NOQA
        self.assertEqual(SupportEmails.save.call_count, 1) #NOQA

    def test_can_only_create_one_instance_of_social_media_links(self):
        with self.assertRaisesMessage(ValidationError, ("Can only create one instance of Support emails. "
                                                        "Please add any additional emails to the previous one created")):
            SupportEmails.objects.create()
            SupportEmails.objects.create()



class SupportEmailTest(TestCase):

    @patch("snippets.models.SupportEmail.save", MagicMock(name="save"))
    def test_can_create(self):
        emails = SupportEmails.objects.create()
        email = SupportEmail(email="support@gmail.com", parent=emails)
        email.save()

        self.assertTrue(SupportEmail.save.called) #NOQA
        self.assertEqual(SupportEmail.save.call_count, 1) #NOQA

    def test_string_representation(self):
        emails = SupportEmails.objects.create()
        email = SupportEmail(email="support@gmail.com", parent=emails)

        self.assertEqual(str(email), "support@gmail.com")
        

class SocialMediaLinksTest(TestCase):
  
    @patch("snippets.models.SocialMediaLinks.save", MagicMock(name="save"))
    def test_can_create_social_media_link(self):
        link = SocialMediaLinks()
        link.save()

        self.assertTrue(SocialMediaLinks.save.called) #NOQA
        self.assertEqual(SocialMediaLinks.save.call_count, 1) #NOQA
    
    def test_can_only_create_one_instance_of_social_media_links(self):
        with self.assertRaisesMessage(ValidationError, ("Can only create one instance of Social media links. "
                                                        "Please add any additional links to the previous one created")):
            SocialMediaLinks.objects.create()
            SocialMediaLinks.objects.create()

    def test_verbose_Name_plural(self):
        self.assertEqual(SocialMediaLinks._meta.verbose_name_plural, "social media links")
        


class NewSocialMediaLinksTest(TestCase):

    @patch("snippets.models.NewSocialMediaLink.save", MagicMock(name="save"))
    def test_can_create_social_media_links(self):
        links = SocialMediaLinks.objects.create()
        social_link = NewSocialMediaLink(name="facebook", url="https://www.facebook.com", parent=links)
        social_link.save()

        self.assertTrue(NewSocialMediaLink.save.called) #NOQA
        self.assertEqual(NewSocialMediaLink.save.call_count, 1) #NOQA

    def test_str_representation(self):
        links = SocialMediaLinks.objects.create()
        social_link = NewSocialMediaLink(name="facebook", url="https://www.facebook.com", parent=links)
        self.assertEqual(str(social_link), "facebook", "should be equal to the name")

    def test_verbose_name_plural(self):
        self.assertEqual(NewSocialMediaLink._meta.verbose_name_plural, "new social media links") # NOQA
