from django import template
from ..models import CompanyDetail

register = template.Library()

@register.simple_tag(name="get_company_detail")
def get_company_detail():
    return CompanyDetail.objects.first() #NOQA

@register.simple_tag(name="get_company_addresses")
def company_address():
    detail = CompanyDetail.objects.first()
    if detail:
        return detail.get_addresses()

@register.simple_tag(name="get_company_phone_numbers")
def company_phone_numbers():
    detail = CompanyDetail.objects.first()
    if detail:
        return detail.get_phone_numbers()

@register.inclusion_tag("contact/_render_company_detail.html", name="render_company_detail")
def render_company_detail():
    company_detail = CompanyDetail.objects.first()
    return {"company_detail": company_detail}

