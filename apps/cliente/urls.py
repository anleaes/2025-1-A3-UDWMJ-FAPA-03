from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path("adicionar/", views.create_cliente, name="cadastroCliente"),
    path("", views.list_clientes, name="list_clientes"),
    path("editar/<int:id_cliente>/", views.edit_cliente, name="edit_cliente"),
    path("excluir/<int:id_cliente>/", views.delete_cliente, name="delete_cliente"),
    path("buscar/", views.search_clients, name="search_clients"),
]
