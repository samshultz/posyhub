from django.test import TestCase
from django.template import Template, Context
from services.models import Service

class TemplateTagsTest(TestCase):
    
    def create_services(self):
        service = Service(name="A new name", description="A new description")
        service.save()
        service2 = Service(name="Another new name", description="Another new description")
        service2.save()
        service3 = Service(name="Yet Another new name", description="Another new description")
        service3.save()
        return service, service2, service3

    def test_get_services_without_params_returns_all_services_in_db(self):
         
        self.create_services()

        template = Template("{% load services_tags %}"
            "{% get_services as services %}"
            "{% for service in services %}"
                "<span>{{ service.name }}</span>"
            "{% endfor %}"
        )
        rendered = template.render(Context({}))

        self.assertIn("<span>A new name</span>", rendered)
        self.assertIn("<span>Another new name</span>", rendered)

    def test_get_services_can_accept_params(self):
        self.create_services()
        
        template = Template("{% load services_tags %}"
            "{% get_services 2 as services %}"
            "{% for service in services %}"
                "<span>{{ service.name }}</span>"
            "{% endfor %}"
        )
        rendered = template.render(Context({}))

        self.assertIn("<span>A new name</span>", rendered)
        self.assertIn("<span>Another new name</span>", rendered)
        
    def test_get_services_returns_num_of_items_specified_in_params(self):
        """ get_services should return only two items when called like this

        {% get_services 2 as services %}

        """

        self.create_services()
        template = Template("{% load services_tags %}"
            "{% get_services 2 as services %}"
            "{% for service in services %}"
                "<span>{{ service.name }}</span>"
            "{% endfor %}"
        )
        rendered = template.render(Context({}))

        
        self.assertNotIn("<span>Yet Another new name</span>", rendered)

    def test_get_services_returns_Nothing_when_no_items_in_db(self):
        template = Template("{% load services_tags %}"
            "{% get_services 2 as services %}"
            "{% for service in services %}"
                "<span>{{ service.name }}</span>"
            "{% endfor %}"
        )
        rendered = template.render(Context({}))
        self.assertEqual("", rendered)
