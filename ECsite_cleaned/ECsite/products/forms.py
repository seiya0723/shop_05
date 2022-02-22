from django import forms
from .models import ProductCategory, Product, ProductImage

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'stock', 'image', 'description', 'price', 'situation']

class ProductsImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'product']

class EditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'stock', 'image', 'description', 'price', 'situation']
