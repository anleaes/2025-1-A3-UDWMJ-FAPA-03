from django.shortcuts import get_object_or_404, redirect, render

from apps.nutricionista.forms import NutricionistaForm
from apps.nutricionista.models import Nutricionista


# Create your views here.
def create_nutricionista(request):
    template_name = "nutricionista/cadastroNutricionista.html"
    context = {}
    if request.method == "POST":
        form = NutricionistaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect("nutricionista:list_nutricionistas")
    form = NutricionistaForm()
    context["form"] = form
    return render(request, template_name, context)


def list_nutricionistas(request):
    template_name = "nutricionista/list_nutricionistas.html"
    nutricionista = Nutricionista.objects.filter()
    context = {
        "nutricionista": nutricionista,
    }
    return render(request, template_name, context)


def edit_nutricionista(request, id_nutricionista):
    template_name = "nutricionista/editNutricionista.html"
    context = {}
    nutricionista = get_object_or_404(Nutricionista, id=id_nutricionista)
    if request.method == "POST":
        form = NutricionistaForm(request.POST, instance=nutricionista)
        if form.is_valid():
            form.save()
            return redirect("nutricionista:list_nutricionistas")
    form = NutricionistaForm(instance=nutricionista)
    context["form"] = form
    return render(request, template_name, context)


def delete_nutricionista(request, id_nutricionista):
    client = Nutricionista.objects.get(id=id_nutricionista)
    client.delete()
    return redirect("nutricionista:list_nutricionistas")
