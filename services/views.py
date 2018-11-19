from django.views.generic import DetailView, ListView
from .models import Service


class ServiceListView(ListView):
    model = Service
    template_name="services/service_list.html"


class ServiceDetailView(DetailView):
    model = Service
    template_name="services/service_detail.html"