from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path("adicionar/", views.create_cliente, name="cadastroCliente"),
    path("", views.list_clientes, name="list_clientes"),
]
