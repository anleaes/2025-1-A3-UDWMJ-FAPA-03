from apps.accounts import forms
from apps.dieta.models import Dieta, DietaAlimento


class DietaForm(forms.ModelForm):

    class Meta:
        model = Dieta


class DietaAlimentoForm(forms.ModelForm):

    class Meta:
        model = DietaAlimento
