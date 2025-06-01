from django import forms
from .models import AdicionaisPagos


class AdicionaisPagoForm(forms.ModelForm):

    class Meta:
        model = AdicionaisPagos
        exclude = (
            "created_on",
            "updated_on",
        )

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "preco": forms.NumberInput(attrs={"class": "form-control form-control-lg"}),
        }

