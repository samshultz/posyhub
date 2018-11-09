from django.test import TestCase
from django.template import Context, Template
from snippets.models import SocialMediaLinks, NewSocialMediaLink


class TemplateTagTest(TestCase):

    def test_template_tag_returns_expected_result(self):

        snips = SocialMediaLinks.objects.create()
        facebook = NewSocialMediaLink.objects.create(name="facebook", url="https://www.facebook.com", parent=snips)
        template = Template("{% load snippets_tags %} "
            "{% get_social_media_links as links %} "
            "{% for link in links %} {{ link.name }} {% endfor %}")
        rendered = template.render(Context({}))

        self.assertIn(facebook.name, rendered)