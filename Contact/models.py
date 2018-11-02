from django.db import models
from django.core.validators import validate_email

class CompanyDetail(models.Model):
    name = models.CharField("Company's Name", max_length=300)
    phone_no = models.CharField("Phone Number",
                                max_length=500,
                                help_text=("if your company has more than one"
                                           " phone number, separate them with"
                                           " a comma"))
    email = models.CharField("Email Addresses", blank=True,
                             max_length=500,
                             help_text=("If your company has more than one"
                                        " email separate them by a comma"))


    def clean(self):
        if self.email:
            email_list = self.get_emails()
            for email in email_list:
                validate_email(email)

    def get_emails(self):
        email = '' if not self.email else [email.strip() for email in self.email.split(",")]
        return email

    def get_phone_numbers(self):
        return [num.strip() for num in self.phone_no.split(",")]

    def get_addresses(self):
        return [addr.address for addr in self.address.all()]

    def save(self, *args, **kwargs):
        self.clean()
        super(CompanyDetail, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class CompanyAddress(models.Model):
    company = models.ForeignKey(CompanyDetail,
                                related_name="address",
                                on_delete=models.DO_NOTHING)   
    address = models.TextField()


    class Meta:
        verbose_name_plural = "company addresses"

    def __str__(self):
        return self.company.name