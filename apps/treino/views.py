from multiprocessing.connection import Client
from django.shortcuts import redirect, render

from apps.treino.forms import TreinoForm


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
