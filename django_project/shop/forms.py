from django import forms
from .models import Product, Category, Order

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price']

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('quantity',)