from django import forms
from .models import ContactFormEntry, EmailAdressFrom

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormEntry
        fields = ('FirstName', 'LastName', 'EmailAddress', 'PhoneNo', 'Message')


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailAdressFrom
        fields = ('EmailAddress',)
