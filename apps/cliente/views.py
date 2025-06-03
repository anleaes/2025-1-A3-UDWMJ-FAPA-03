from django.shortcuts import render, redirect
from .models import Cliente, AdicionaisPagos, ItemCliente
from .forms import ClienteForm


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
            return redirect(
                "cliente:list_clientes"
            )  # depois criar uma tela escrito HomeCliente
    form = ClienteForm()
    context["form"] = form
    return render(request, template_name, context)


def list_clientes(request):
    template_name = "cliente/list_clientes.html"
    item_cliente = ItemCliente.objects.filter()
    adicionaisPagos = AdicionaisPagos.objects.filter()
    clientes = Cliente.objects.filter()
    context = {
        "cliente": clientes,
        "adicionaisPagos": adicionaisPagos,
        "item_cliente": item_cliente,
    }
    return render(request, template_name, context)
