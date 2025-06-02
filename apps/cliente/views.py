from django.shortcuts import render, redirect
from .models import Cliente, AdicionaisPagos, ItemCliente
from forms import ClienteForm


# Create your views here.
def create_cliente(request):
    template_name = "cliente/cadastroCliente.html"
    context = {}
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect("core:Home")  # depois criar uma tela escrito HomeCliente
    form = ClienteForm()
    context["form"] = form
    return render(request, template_name, context)
