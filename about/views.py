from django.shortcuts import render
from django.views.generic import TemplateView
from about.models import AboutCompany

class DisplayAboutView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayAboutView, self).get_context_data(**kwargs)
        context['about'] = AboutCompany.objects.first()
        return context