"""
URL configuration for GerenciamentoAcademiaDietaApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("cliente/", include("cliente.urls", namespace="cliente")),
    path("adicionalPago/", include("adicionaispago.urls", namespace="adicionaisPago")),
    path("contas/", include("accounts.urls", namespace="accounts")),
    path("personal/", include("personal.urls", namespace="personal")),
    path("nutricionista/", include("nutricionista.urls", namespace="nutricionista")),
    path("treino/", include("treino.urls", namespace="treino")),
    path("dieta/", include("dieta.urls", namespace="dieta")),
    path("alimento/", include("alimento.urls", namespace="alimento")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
