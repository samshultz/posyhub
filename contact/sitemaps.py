from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import CompanyDetail


class ContactSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9
  
    def items(self):
        return CompanyDetail.objects.all() #NOQA

    def location(self, obj):
        return reverse("contact:contact-us")