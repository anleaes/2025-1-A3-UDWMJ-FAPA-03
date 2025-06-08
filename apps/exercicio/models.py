from django.db import models


# Create your models here.
class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    grupo_muscular = models.CharField(max_length=50)
    duracao_minutos = models.IntegerField()
