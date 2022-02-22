from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['profile_image', 'username', "email", 'name', 'name_kana']

class AccountEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'username']