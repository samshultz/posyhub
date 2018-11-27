from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service


class ServiceSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9
  
    def items(self):
        return Service.objects.all() #NOQA