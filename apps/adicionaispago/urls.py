from django.urls import path
from . import views

app_name = "adicionaisPago"


urlpatterns = [
    path("adicionar/", views.add_adicionalPago, name="add_adicionalPago"),
]
