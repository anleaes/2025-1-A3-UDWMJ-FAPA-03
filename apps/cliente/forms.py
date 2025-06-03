from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        exclude = ()

        widgets = {
            "primeiro_nome": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "segundo_nome": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "email": forms.EmailInput(attrs={"class": "form-control form-control-lg"}),
            "endereco": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "genero": forms.Select(attrs={"class": "form-select form-select-lg"}),
            "item_cliente": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
        }
