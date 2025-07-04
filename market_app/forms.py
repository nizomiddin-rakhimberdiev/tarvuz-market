from django import forms
from .models import Product, Category
from users.models import CustomUser

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'email']

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category', 'image']

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']