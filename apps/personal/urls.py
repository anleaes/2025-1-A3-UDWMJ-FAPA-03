from django.urls import path
from . import views

app_name = "personal"

urlpatterns = [
    path("adicionar/", views.create_personal, name="cadastroPersonal"),
    path("", views.list_personais, name="list_personais"),
    path("editar/<int:id_personal>/", views.edit_personal, name="editPersonal"),
    path("excluir/<int:id_personal>/", views.delete_personal, name="delete_personal"),
]
