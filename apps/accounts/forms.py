from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "email"]

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "password": forms.PasswordInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "email": forms.EmailInput(attrs={"class": "form-control form-control-lg"}),
        }


class UserChangeInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "email": forms.EmailInput(attrs={"class": "form-control form-control-lg"}),
        }
