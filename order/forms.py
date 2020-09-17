from django import forms

from .models import Order
from shop.models import buyingList

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = buyingList
        fields = ['name', 'price', 'stock']