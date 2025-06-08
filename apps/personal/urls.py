from django.urls import path
from . import views

app_name = "personal"

urlpatterns = [path("adicionar/", views.create_personal, name="cadastroPersonal")]
