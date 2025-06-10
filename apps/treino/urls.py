from django.urls import path
from . import views

app_name = "treino"

urlpatterns = [
    path("adicionar/<int:id_cliente>/", views.add_treino, name="add_treino"),
    path("", views.list_treinos, name="list_treinos"),
    path("delete/<int:id_treino>/", views.delete_treino, name="delete_treino"),
    path(
        "add-exercicio/<int:id_treino>/",
        views.add_treino_exercicio,
        name="add_treino_exercicio",
    ),
    path(
        "delete-exercicio/<int:id_te>/",
        views.delete_treino_exercicio,
        name="delete_treino_exercicio",
    ),
]
