from django.urls import path
from . import views

app_name = "adicionaisPago"


urlpatterns = [
    path("adicionar/", views.add_adicionalPago, name="add_adicionalPago"),
    path("", views.list_adicionaisPagos, name="list_adicionaisPagos"),
    path(
        "editar/<int:id_adicional>/",
        views.edit_adicionalPago,
        name="edit_adicionalPago",
    ),
    path(
        "excluir/<int:id_adicional>/", views.delete_adicional, name="delete_adicional"
    ),
]
