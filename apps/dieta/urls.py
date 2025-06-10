from django.urls import path
from . import views

app_name = "dieta"

urlpatterns = [
    path("adicionar/<int:id_cliente>/", views.add_dieta, name="add_dieta"),
    path("", views.list_dietas, name="list_dietas"),
    path("delete/<int:id_dieta>/", views.delete_dieta, name="delete_dieta"),
    path(
        "add-alimento/<int:id_dieta>/",
        views.add_dieta_alimento,
        name="add_dieta_alimento",
    ),
    path(
        "delete-alimento/<int:id_da>/",
        views.delete_dieta_alimento,
        name="delete_dieta_alimento",
    ),
]
