from django.db import models
from adicionaispago.models import AdicionaisPagos

# Create your models here.


class Cliente(models.Model):
    primeiro_nome = models.CharField("Primeiro-Nome", max_length=150)
    segundo_nome = models.CharField("Segundo-Nome", max_length=150)
    endereco = models.CharField("Endereco", max_length=150)
    email = models.EmailField("Email", null=False, blank=False)
    GENEROS = (("M", "Masculino"), ("F", "Feminino"), ("O", "Outro"))
    genero = models.CharField("Genenro", max_length=1, choices=GENEROS)
    item_cliente = models.ManyToManyField(
        AdicionaisPagos, through="ItemCliente", blank=True
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["id"]

    def __str__(self):
        return self.first_name


class ItemCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    adicionaisPago = models.ForeignKey(AdicionaisPagos, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Item Adicional Pago"
        verbose_name_plural = "Itens Adicionais Pagos"
        ordering = ["id"]

    def __str__(self):
        return self.socialnetwork.name
