from django.db import models

from apps.exercicio.models import Exercicio


# Create your models here.
class Treino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    exercicios = models.ManyToManyField(
        "exercicio.Exercicio",
        through="TreinoExercicio",
        blank=True,
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Treino"
        verbose_name_plural = "Treinos"
        ordering = ["-criado_em"]

    def __str__(self):
        return self.nome


class TreinoExercicio(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    exercicio = models.ForeignKey("exercicio.Exercicio", on_delete=models.CASCADE)
    series = models.PositiveIntegerField("Séries", default=3)
    repeticoes = models.PositiveIntegerField("Repetições", default=10)
    carga = models.DecimalField(
        "Carga (kg)", max_digits=5, decimal_places=2, null=True, blank=True
    )
    observacao = models.TextField("Observação", blank=True)

    class Meta:
        verbose_name = "Exercício do Treino"
        verbose_name_plural = "Exercícios do Treino"
        ordering = ["id"]

    def __str__(self):
        return f"{self.exercicio.nome} - {self.treino.nome}"
