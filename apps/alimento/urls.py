from django.urls import path
from . import views

app_name = "alimento"

urlpatterns = [
    path("", views.list_alimentos, name="list_alimentos"),
    path("adicionar/", views.add_alimento, name="add_alimento"),
    path("editar/<int:id_alimento>/", views.edit_alimento, name="edit_alimento"),
    path("excluir/<int:id_alimento>/", views.delete_alimento, name="delete_alimento"),
]
