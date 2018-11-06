from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact-us/', include('contact.urls', namespace="contact")),
    url(r'^about/', include('about.urls', namespace="about")),
    url(r'^services/', include('services.urls', namespace="services"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)