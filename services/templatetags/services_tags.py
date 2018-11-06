from django import template
from services.models import Service

register = template.Library()


@register.simple_tag(name="get_services")
def services(num=None):
    return Service.objects.all()[:num]