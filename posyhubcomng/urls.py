from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib.sitemaps.views import index
from django.contrib.sitemaps.views import sitemap

from zinnia.sitemaps import AuthorSitemap #NOQA
from zinnia.sitemaps import CategorySitemap #NOQA
from zinnia.sitemaps import EntrySitemap #NOQA
from zinnia.sitemaps import TagSitemap #NOQA

from about.sitemaps import AboutSitemap
from contacts.sitemaps import ContactSitemap
from services.sitemaps import ServiceSitemap

sitemaps = {

    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap,
    'about': AboutSitemap,
    'contacts': ContactSitemap,
    'services': ServiceSitemap
}

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^contact-us/', include('contacts.urls', namespace="contact")),
    url(r'^about/', include('about.urls', namespace="about")),
    url(r'^services/', include('services.urls', namespace="services")),
    url(r'^blog/', include('zinnia.urls', namespace="blog")),
    url(r'^blog/comments/', include('fluent_comments.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^sitemap\.xml$', index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^sitemap\.html$', include('zinnia.urls.sitemap')),
    url(r'^$', TemplateView.as_view(template_name="posyhub/index.html"), name="home")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)