from django import forms

from apps.personal.models import Personal


class PersonalForm(forms.ModelForm):

    class Meta:
        model = Personal
        exclude = ()

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        }
