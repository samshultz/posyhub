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
        # Ensure that only one instance of this model can be created
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
