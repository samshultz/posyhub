from django.shortcuts import render
from django.views.generic import DetailView
from .models import Service


class ServiceDetailView(DetailView):
    model = Service