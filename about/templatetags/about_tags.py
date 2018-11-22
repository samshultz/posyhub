from django import template
from about.models import AboutCompany

register = template.Library()


@register.simple_tag(name="get_company_description")
def get_about_company():
    about = AboutCompany.objects.first()
    if about:
        return about.content