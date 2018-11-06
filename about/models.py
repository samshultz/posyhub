from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AboutCompany(models.Model):
    content = models.TextField(blank=False)

    class Meta:
        verbose_name_plural = _('about company')
    def __str__(self):
        return _("About company")

    def save(self, *args, **kwargs):
        if not self.content:
            raise ValidationError(_("You must enter a description of your company"), code='Invalid Entry')
        super(AboutCompany, self).save(*args, **kwargs) # Call the real save() method
