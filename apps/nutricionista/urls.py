from django.urls import path
from . import views

app_name = "nutricionista"

urlpatterns = [
    path("adicionar/", views.create_nutricionista, name="cadastroNutricionista"),
    path("", views.list_nutricionistas, name="list_nutricionistas"),
    path(
        "editar/<int:id_nutricionista>/",
        views.edit_nutricionista,
        name="editNutricionista",
    ),
    path(
        "excluir/<int:id_nutricionista>/",
        views.delete_nutricionista,
        name="delete_nutricionista",
    ),
]
