from django import forms
from .models import Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'amount']

class CartEditForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['amount']