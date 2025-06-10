# from accounts import forms
from django import forms
from dieta.models import Dieta, DietaAlimento


class DietaForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = ["nome", "descricao", "nutricionista"]


class DietaAlimentoForm(forms.ModelForm):
    class Meta:
        model = DietaAlimento
        fields = ["alimento", "quantidade"]
