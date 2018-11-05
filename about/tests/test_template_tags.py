from django.template import Template, Context
from django.test import TestCase
from about.models import AboutCompany


class TemplateTagTests(TestCase):

    def test_get_company_description_renders(self):
        abt = AboutCompany.objects.create(content="A Very long Text")
        template = Template("{% load about_tags %} {% get_company_description as desc %} {{ desc }}")
        rendered = template.render(Context({}))

        self.assertIn(abt.content, rendered)