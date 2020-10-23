from django import forms


class AddProductForm(forms.Form):
    quantity = forms.IntegerField(label="수량 ")
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)