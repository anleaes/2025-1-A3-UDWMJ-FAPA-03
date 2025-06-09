from multiprocessing.connection import Client
from django.shortcuts import get_object_or_404, redirect, render

from apps.treino.forms import TreinoExercicioForm, TreinoForm
from apps.treino.models import Treino, TreinoExercicio


# Create your views here.
def add_treino(request, id_client):
    template_name = "treino/add_treino.html"
    context = {}
    if request.method == "POST":
        form = TreinoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.client = Client.objects.get(id=id_client)
            f.save()
            form.save_m2m()
            return redirect("treino:list_treinos")
    form = TreinoForm()
    context["form"] = form
    return render(request, template_name, context)


def list_treinos(request):
    template_name = "treinos/list_treinos.html"
    treinos = Treino.objects.all()
    context = {"treinos": treinos}
    return render(request, template_name, context)


def delete_treino(request, id_treino):
    treino = get_object_or_404(Treino, id=id_treino)
    treino.delete()
    return redirect("treinos:list_treinos")


def add_treino_exercicio(request, id_treino):
    template_name = "treinos/add_treino_exercicio.html"
    context = {}
    if request.method == "POST":
        form = TreinoExercicioForm(request.POST)
        if form.is_valid():
            te = form.save(commit=False)
            te.treino = get_object_or_404(Treino, id=id_treino)
            te.save()
            return redirect("treinos:list_treinos")
    else:
        form = TreinoExercicioForm()
    context["form"] = form
    return render(request, template_name, context)


def delete_treino_exercicio(request, id_te):
    te = get_object_or_404(TreinoExercicio, id=id_te)
    te.delete()
    return redirect("treinos:list_treinos")
