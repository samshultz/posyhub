from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib import messages


class SocialMediaLinks(models.Model):
    """
    Model definition for SocialMediaLinks.

    Helps you keep track of of the company's social media pages
    """

    class Meta:

        verbose_name_plural = 'social media links'

    def __str__(self):
        return "Social Media Links"

    def save(self, *args, **kwargs):
        if SocialMediaLinks.objects.exists() and not self.pk:
            raise ValidationError(_("Can only create one instance of Social media links. "
                                     "Please add any additional links to the previous one created"))
        super(SocialMediaLinks, self).save(*args, **kwargs) # Call the real save() method


class NewSocialMediaLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(_("Link"), max_length=300)
    parent = models.ForeignKey(SocialMediaLinks, related_name="links", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            super(NewSocialMediaLink, self).save(*args, **kwargs) # Call the real save() method
        except ValueError:
            return


class SupportEmails(models.Model):
    class Meta:
        verbose_name_plural = "support emails"
    
    def __str__(self):
        return "Support Emails"

    def save(self, *args, **kwargs):
        if SupportEmails.objects.exists() and not self.pk:
            raise ValidationError(_("Can only create one instance of Support emails. "
                                     "Please add any additional emails to the previous one created"))
        super(SupportEmails, self).save(*args, **kwargs) # Call the real save() method


class SupportEmail(models.Model):

    email = models.EmailField()
    parent = models.ForeignKey(SupportEmails, on_delete=models.CASCADE, related_name="emails")

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        try:
            super(SupportEmail, self).save(*args, **kwargs) # Call the real save() method
        except ValueError:
            return