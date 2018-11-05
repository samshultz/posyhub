from django import template
from contact.models import CompanyDetail

register = template.Library()

@register.simple_tag(name="get_company_detail")
def get_company_detail():
    return CompanyDetail.objects.first()

@register.simple_tag(name="get_company_addresses")
def company_address():
    return CompanyDetail.objects.first().get_addresses()

@register.inclusion_tag("contact/_render_company_detail.html", name="render_company_detail")
def render_company_detail():
    company_detail = CompanyDetail.objects.first()
    return {"company_detail": company_detail}

