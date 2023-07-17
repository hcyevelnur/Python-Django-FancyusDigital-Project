from django import forms
from .models import FaqFormEntry

class FaqForm(forms.ModelForm):
    class Meta:
        model = FaqFormEntry
        fields = ('FirstName', 'EmailAddress', 'PhoneNo', 'Message')