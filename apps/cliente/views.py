from django.shortcuts import get_object_or_404, render, redirect
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


def edit_cliente(request, id_cliente):
    template_name = "cliente/cadastroCliente.html"
    context = {}
    client = get_object_or_404(Cliente, id=id_cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("cliente:list_clientes")
    form = ClienteForm(instance=client)
    context["form"] = form
    return render(request, template_name, context)


def delete_cliente(request, id_cliente):
    client = Cliente.objects.get(id=id_cliente)
    client.delete()
    return redirect("cliente:list_clientes")
