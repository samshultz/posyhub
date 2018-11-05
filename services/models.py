from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="services/%Y/%m/%d/", blank=True)
    description = models.TextField(default='')  