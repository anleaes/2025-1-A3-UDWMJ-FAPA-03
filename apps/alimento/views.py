from django.shortcuts import get_object_or_404, redirect, render

from alimento.forms import AlimentoForm
from alimento.models import Alimento


# Create your views here.
def add_alimento(request):
    template_name = "alimento/add_alimento.html"
    context = {}
    if request.method == "POST":
        form = AlimentoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect("alimento:list_alimentos")
    form = AlimentoForm()
    context["form"] = form
    return render(request, template_name, context)


def list_alimentos(request):
    template_name = "alimento/list_alimentos.html"
    alimentos = Alimento.objects.filter()
    context = {"alimentos": alimentos}
    return render(request, template_name, context)


def edit_alimento(request, id_alimento):
    template_name = "alimento/add_alimento.html"
    context = {}
    alimentos = get_object_or_404(Alimento, id=id_alimento)
    if request.method == "POST":
        form = AlimentoForm(request.POST, request.FILES, instance=alimentos)
        if form.is_valid():
            form.save()
            return redirect("alimento:list_alimentos")
    form = AlimentoForm(instance=alimentos)
    context["form"] = form
    return render(request, template_name, context)


def delete_alimento(request, id_alimento):
    product = Alimento.objects.get(id=id_alimento)
    product.delete()
    return redirect("alimento:list_alimentos")
