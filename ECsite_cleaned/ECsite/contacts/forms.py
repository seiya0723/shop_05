from django import forms
from .models import Contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['user_id', 'name', 'email', 'title', 'contents']
