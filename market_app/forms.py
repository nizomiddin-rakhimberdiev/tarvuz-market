from django import forms
from .models import Product, Category

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category', 'image']

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']