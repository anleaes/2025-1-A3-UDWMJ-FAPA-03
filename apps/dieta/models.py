from django.db import models

from django.db import models
from cliente.models import Cliente
from apps.nutricionista.models import Nutricionista
from alimento.models import Alimento


# Create your models here.
class Dieta(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(
        Nutricionista, on_delete=models.SET_NULL, null=True
    )
    alimentos = models.ManyToManyField(Alimento, through="DietaAlimento")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class DietaAlimento(models.Model):
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    quantidade = models.CharField(max_length=50)
    horario = models.CharField(max_length=50, help_text="Ex: Café da manhã, Almoço...")

    def __str__(self):
        return f"{self.alimento.nome} - {self.dieta.nome}"
