from django.conf.urls import url
from services.views import ServiceDetailView, ServiceListView


urlpatterns = [
    url(r'^$', ServiceListView.as_view(), name="services_list"),
    url(r'^(?P<slug>[-\w]+)/$', ServiceDetailView.as_view(), name="service_detail"),
]
