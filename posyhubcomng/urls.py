from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^contact-us/', include('contact.urls', namespace="contact")),
    url(r'^about/', include('about.urls', namespace="about")),
    url(r'^services/', include('services.urls', namespace="services")),
    url(r'^blog/', include('zinnia.urls', namespace="blog")),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', TemplateView.as_view(template_name="posyhub/index.html"), name="home")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)