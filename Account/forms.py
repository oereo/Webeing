from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
#from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)
    #phone_number = PhoneNumberField(_("Phone (Please state your country code eg. +44)"))
    nickname = forms.CharField(label = 'nickname')
    class Meta:
        model = User
        fields = ('email', 'nickname', 'date_of_birth')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth','nickname',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]