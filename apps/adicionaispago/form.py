from django import forms
from .models import AdicionaisPagos


class AdicionaisPagoForm(forms.ModelForm):

    class Meta:
        model = AdicionaisPagos
        exclude = (
            "created_on",
            "updated_on",
        )
