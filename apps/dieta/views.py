from django.shortcuts import get_object_or_404, redirect, render

from cliente.models import Cliente
from dieta.forms import DietaAlimentoForm, DietaForm
from dieta.models import Dieta, DietaAlimento


# Create your views here.
def add_dieta(request, id_cliente):
    template_name = "dieta/add_dieta.html"
    context = {}
    if request.method == "POST":
        form = DietaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.cliente = Cliente.objects.get(id=id_cliente)
            f.save()
            form.save_m2m()
            return redirect("dieta:list_dietas")
    form = DietaForm()
    context["form"] = form
    return render(request, template_name, context)


def list_dietas(request):
    template_name = "dieta/list_dietas.html"
    dietas = Dieta.objects.all()
    context = {"dietas": dietas}
    return render(request, template_name, context)


def delete_dieta(request, id_dieta):
    treino = get_object_or_404(Dieta, id=id_dieta)
    treino.delete()
    return redirect("dieta:list_dietas")


def add_dieta_alimento(request, id_dieta):
    template_name = "dieta/add_dieta_alimento.html"
    context = {}
    if request.method == "POST":
        form = DietaAlimentoForm(request.POST)
        if form.is_valid():
            te = form.save(commit=False)
            te.dieta = get_object_or_404(Dieta, id=id_dieta)
            te.save()
            return redirect("dieta:list_dietas")
    else:
        form = DietaAlimentoForm()
    context["form"] = form
    return render(request, template_name, context)


def delete_dieta_alimento(request, id_dieta):
    te = get_object_or_404(DietaAlimento, id=id_dieta)
    te.delete()
    return redirect("dieta:list_dietas")
