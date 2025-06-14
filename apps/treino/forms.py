from django import forms

from .models import Treino, TreinoExercicio


class TreinoForm(forms.ModelForm):

    class Meta:
        model = Treino
        exclude = ("client", "treino")


class TreinoExercicioForm(forms.ModelForm):

    class Meta:
        model = TreinoExercicio
        exclude = ("order",)
