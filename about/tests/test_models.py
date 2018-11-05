from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.core.exceptions import ValidationError

from about.models import AboutCompany


class AboutCompanyTest(TestCase):

    @patch("about.models.AboutCompany.save", MagicMock(name='save'))
    def test_can_save_about_content(self):
        abt = AboutCompany(content="This is a long text about us")
        abt.save()

        self.assertTrue(AboutCompany.save.called) # NOQA
        self.assertEqual(AboutCompany.save.call_count, 1) #NOQA
    
    def test_cant_save_with_invalid_data(self):
        about = AboutCompany()

        with self.assertRaisesMessage(ValidationError, "You must enter a description of your company"):
            about.save()

    def test_string_representation(self):
        about = AboutCompany(content="This is a long text about us")

        self.assertEqual(str(about), "About company")
    
    def test_verbose_name_plural(self):
        self.assertEqual(AboutCompany._meta.verbose_name_plural, "about company") # NOQA