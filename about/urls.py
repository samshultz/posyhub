from django.conf.urls import url
from about.views import DisplayAboutView


urlpatterns = [
    url(r'^$', DisplayAboutView.as_view(), name="about-us")
]