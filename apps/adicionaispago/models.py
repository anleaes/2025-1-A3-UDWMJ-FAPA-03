from django.db import models


# Create your models here.
class AdicionaisPagos(models.Model):
    nome = models.CharField(("Nome"), max_length=50)
    preco = models.FloatField("Preço")
    widgets = {
        "nome": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        "preco": forms.NumberInput(attrs={"class": "form-control form-control-lg"}),
    }

    class Meta:
        verbose_name = "adicionaispago"
        verbose_name_plural = "adicionaispagos"

    def __str__(self):
        return self.name
