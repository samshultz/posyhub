from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact-us/', include('contact.urls', namespace="contact")),
    url(r'^about/', include('about.urls', namespace="about")),
    url(r'^services/', include('services.urls', namespace="services"))
]
