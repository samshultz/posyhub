from django.test import TestCase
from contact.models import CompanyDetail, CompanyAddress
from django.core.exceptions import ValidationError

class CompanyDetailTest(TestCase):

    def test_string_representation(self):
        company_detail = CompanyDetail(
                name="Posyhub international",
                phone_no="08163143403",
                email="taiwogabrielsamuel@gmail.com"
        )
        self.assertEqual(str(company_detail), "Posyhub international")

    def test_get_emails_returns_a_list(self):
        """
            test that the get email method returns a list

        """
        company_detail = CompanyDetail(
                name="Posyhub international",
                phone_no="08163143403",
                email="taiwogabrielsamuel@gmail.com"
            )
        self.assertTrue(isinstance(company_detail.get_emails(), list))

    def test_get_emails_returns_a_string_when_email_is_absent(self):
        company_detail = CompanyDetail(
                name="Posyhub international",
                phone_no="08163143403",
        )
        self.assertTrue(isinstance(company_detail.get_emails(), str))

    def test_get_emails_returns_a_list_with_one_item(self):
        """ tests that get_emails method returns a list with one
        item when only one email exists.
        """
        company_detail = CompanyDetail(
                name="Posyhub international",
                phone_no="08163143403",
                email="taiwogabrielsamuel@gmail.com"
            )

        self.assertTrue(company_detail.get_emails())

    def test_doesnt_raise_a_validation_error_when_no_email_is_entered(self):
        company_detail = CompanyDetail(
                    name="Posyhub international",
                    phone_no="08163143403",
        )
        self.assertTrue(company_detail)

    def test_raises_validation_error_when_user_enters_one_invalid_email(self):


        with self.assertRaises(ValidationError):
            company_detail = CompanyDetail(
                    name="Posyhub international",
                    phone_no="08163143403",
                    email="taiwogabrielsamuel@gmail"
            )
            company_detail.save()

    def test_raises_validation_error_with_more_than_one_invalid_email(self):
        with self.assertRaises(ValidationError):
            company_detail = CompanyDetail(
                    name="Posyhub international",
                    phone_no="08163143403",
                    email="taiwogabrielsamuel@gmail, admin@posyhub.com"
            )
            company_detail.save()

    def test_get_phone_numbers_returns_a_list_of_one_item(self):
        """ get_phone_numbers returns a list of one item if only one phone
        number is provided"""

        company_detail = CompanyDetail(
                    name="Posyhub international",
                    phone_no="08163143403",
                    email="taiwogabrielsamuel@gmail.com, admin@posyhub.com"
            )

        self.assertTrue(isinstance(company_detail.get_phone_numbers(), list))
        self.assertTrue(company_detail.get_phone_numbers())
        self.assertEqual(len(company_detail.get_phone_numbers()), 1)

    def test_get_phone_numbers_returns_a_list_gt_one_item_if_gt_one_item_is_given(self):
        company_detail = CompanyDetail(
                    name="Posyhub international",
                    phone_no="08165443403, +234816123308",
                    email="taiwogabrielsamuel@gmail.com, admin@posyhub.com"
            )
        self.assertGreater(len(company_detail.get_phone_numbers()), 1)

    def test_get_addresses_returns_list_of_addresses(self):
        company = CompanyDetail(
                    name="Posyhub international",
                    phone_no="08165443403, +234816123308",
                    email="taiwogabrielsamuel@gmail.com, admin@posyhub.com"
            )

        CompanyAddress(
            company=company,
            address="A very long address"
            )
        self.assertTrue(isinstance(company.get_addresses(), list))

class CompanyAddressTest(TestCase):
    def test_string_representation(self):
        company = CompanyDetail(
                    name="Posyhub international",
                    phone_no="08165443403, +234816123308",
                    email="taiwogabrielsamuel@gmail.com, admin@posyhub.com"
            )

        address = CompanyAddress(
            company=company,
            address="A very long address"
            )
        self.assertEqual(str(address), "Posyhub international")

    def test_verbose_name_plural(self):
        self.assertEqual(CompanyAddress._meta.verbose_name_plural, "company addresses") # NOQA