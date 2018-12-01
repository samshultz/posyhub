from django.test import TestCase
from django.template import Template, Context
from contact.models import CompanyAddress, CompanyDetail

class ContactTemplateTagsTest(TestCase):

    def create_company_detail(self, phone_no="08239849348", email="admin@gmail.com", addr=["207 Chicago, LA"]):
        company_detail = CompanyDetail.objects.create(name="PosyHub", 
            phone_no=phone_no, 
            email=email)
        for ad in addr:
            CompanyAddress.objects.create(company=company_detail, address=ad)
        

        return company_detail

    def test_get_company_detail_tag_renders(self):
        company_detail = self.create_company_detail()
        
        template = Template("{% load contact_tags %} {% get_company_detail as comp_detail %} {{ comp_detail.name }}")
        rendered = template.render(Context({}))
        
        self.assertIn(company_detail.name, rendered)

    def test_render_company_detail_tag_renders(self):
        company_detail = self.create_company_detail()
        
        template = Template("{% load contact_tags %} {% render_company_detail %}")
        rendered = template.render(Context({}))

        self.assertInHTML('<li>Company Name: {}</li>'.format(company_detail.name), rendered)
        self.assertInHTML('<li>08239849348</li>', rendered)
        self.assertInHTML('<li>admin@gmail.com</li>', rendered)
        self.assertInHTML('<li>207 Chicago, LA</li>', rendered)

    def test_multiple_address_is_rendered_in_template(self):
        """
        if there is more than one address for a particular company in the DB
        render_company_detail_tag should_render them in the html as a span tag
        """
        self.create_company_detail(addr=["207 Chicago, LA", "63 New York, LA"])
        
        template = Template("{% load contact_tags %} {% render_company_detail %}")
        rendered = template.render(Context({}))
        self.assertInHTML("<li>207 Chicago, LA</li>", rendered)
        self.assertInHTML("<li>63 New York, LA</li>", rendered)

    def test_multiple_email_is_rendered_in_template(self):
        """
        if there is more than one email address for a particular company in the DB
        render_company_detail_tag should_render them in the html as a span tag
        """

        self.create_company_detail(email="admin@gmail.com, taiwogabrielsamuel@gmail.com")
        template = Template("{% load contact_tags %} {% render_company_detail %}")
        rendered = template.render(Context({}))

        self.assertInHTML("<li>admin@gmail.com</li>", rendered)
        self.assertInHTML("<li>taiwogabrielsamuel@gmail.com</li>", rendered)

    def test_multiple_phone_no_is_rendered_in_template(self):

        """
        if there is more than one email address for a particular company in the DB
        render_company_detail_tag should_render them in the html as a span tag
        """

        self.create_company_detail(phone_no="08239849348, 0392931028")
        
        template = Template("{% load contact_tags %} {% render_company_detail %}")
        rendered = template.render(Context({}))

        self.assertInHTML("<li>08239849348</li>", rendered)
        self.assertInHTML("<li>0392931028</li>", rendered)

    def test_get_company_addresses_renders(self):
        """
        get_company_addresses should return a list of company address
        """
        self.create_company_detail(addr=["207 Chicago, LA", "63 New York, LA"])

        template = Template("{% load contact_tags %}"
            "{% get_company_addresses as addr %}" 
            "{% for i in addr %}{{ i }}{% endfor %}")
        rendered = template.render(Context({}))

        self.assertIn("207 Chicago, LA", rendered)
        self.assertIn("63 New York, LA", rendered)
    
    def test_get_company_phone_numbers_renders(self):
        self.create_company_detail(phone_no="08239849348, 0392931028")

        template = Template("{% load contact_tags %}"
            "{% get_company_phone_numbers as num %}" 
            "{% for i in num %}{{ i }}{% endfor %}")
        rendered = template.render(Context({}))

        self.assertIn("08239849348", rendered)
        self.assertIn("0392931028", rendered)