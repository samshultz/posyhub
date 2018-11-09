from django import template
from snippets.models import SocialMediaLinks

register = template.Library()

@register.simple_tag(name='get_social_media_links')
def social_media_links():
    return SocialMediaLinks.objects.first().links.all()