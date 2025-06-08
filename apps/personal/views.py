from django.shortcuts import get_object_or_404, redirect, render

from apps.personal.forms import PersonalForm
from apps.personal.models import Personal


# Create your views here.
def create_personal(request):
    template_name = "personal/cadastroPersonal.html"
    context = {}
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect("cliente:list_personais")
    form = PersonalForm()
    context["form"] = form
    return render(request, template_name, context)


def list_personais(request):
    template_name = "cliente/list_personais.html"
    personais = Personal.objects.filter()
    context = {
        "personal": personais,
    }
    return render(request, template_name, context)


def edit_personal(request, id_personal):
    template_name = "personal/editarPersonal.html"
    context = {}
    client = get_object_or_404(Personal, id=id_personal)
    if request.method == "POST":
        form = PersonalForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("personal:list_personais")
    form = PersonalForm(instance=client)
    context["form"] = form
    return render(request, template_name, context)


def delete_personal(request, id_personal):
    client = Personal.objects.get(id=id_personal)
    client.delete()
    return redirect("personal:list_personais")
