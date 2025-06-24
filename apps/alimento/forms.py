from django import forms
from .models import Alimento


class AlimentoForm(forms.ModelForm):

    class Meta:
        model = Alimento
        exclude = ()

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "calorias": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "tipo": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        }
