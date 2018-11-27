from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import AboutCompany


class AboutSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9
  
    def items(self):
        return AboutCompany.objects.all() #NOQA

    def location(self, obj):
        return reverse("about:about-us")