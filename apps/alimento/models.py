from django.db import models


# Create your models here.
class Alimento(models.Model):
    nome = models.CharField(max_length=100)
    calorias = models.FloatField()
    tipo = models.CharField(max_length=50)
