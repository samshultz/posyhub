from .models import CompanyDetail
from .forms import ContactForm
from django.views.generic.edit import FormView



class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact/contact.html"
    success_url = '/thanks/'

    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(*args, **kwargs)
        context["contact"] = CompanyDetail.objects.first()
        return context

    def form_valid(self, form):
        form.send_email(form.cleaned_data)
        return super(ContactView, self).form_valid(form)