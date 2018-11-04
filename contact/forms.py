from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):

    name = forms.CharField(label="Your Name*", max_length=100, required=True)
    name_of_business = forms.CharField(label="Name of your company or Business", max_length=100, required=False)
    phone_no = forms.CharField(label="Phone Number*", max_length=50, required=True)
    email = forms.EmailField(label="Email address(if available)", required=False)
    message = forms.CharField(label="Message*", required=True, widget=forms.Textarea)

    def send_email(self, data):
                
        subject = "A new message from {} owner of {}".format(data['name'], 
                                                             data['name_of_business'])
        from_email = data['email'] if data['email'] else 'owner@gmail.com'
        send_mail(subject, data['message'], from_email, ["support@posyhub.com"])
        return True
        