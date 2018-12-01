from django import forms
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):

    name = forms.CharField(label=_("Your Name*"), max_length=100, required=True)
    name_of_business = forms.CharField(label=_("Name of your company or Business"), max_length=100, required=False)
    phone_no = forms.CharField(label=_("Phone Number*"), max_length=50, required=True)
    email = forms.EmailField(label=_("Email address(if available)"), required=False)
    message = forms.CharField(label=_("Message*"), required=True, widget=forms.Textarea)

    def send_email(self, data):
        name = data.get(_('name'), "")
        from_email = data.get(_('email'), 'owner@gmail.com')
        subject = "A new message from {} a potential client".format(name)
        send_mail(subject, data['message'], from_email, ["support@posyhub.com"])
        return True
        