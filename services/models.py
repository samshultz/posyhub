from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Service(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=250, blank=True)
    image = models.ImageField(upload_to="services/%Y/%m/%d/", blank=True)
    description = RichTextUploadingField(default="", config_name="basic")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        
        if not self.name:
            raise ValidationError(_("Name field cannot be empty"), code="invalid")
        
        if not self.description:
            raise ValidationError(_("Description field cannot be empty"), code="invalid")

        if not self.slug:
            self.slug = slugify(self.name)
        
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('services:service_detail', kwargs={'slug': self.slug})

