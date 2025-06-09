from django.shortcuts import get_object_or_404, render, redirect
from .form import AdicionaisPagoForm
from .models import AdicionaisPagos

# Create your views here.


def add_adicionalPago(request):
    template_name = "adicionaisPagos/add_adicionalPago.html"
    context = {}
    if request.method == "POST":
        form = AdicionaisPagoForm(request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.save()
            form.save_m2m()

            return redirect(
                "cliente:list_clientes"
            )  # mudar depois para listar os adicionais

    form = AdicionaisPagoForm()
    context["form"] = form
    return render(request, template_name, context)


def list_adicionaisPagos(request):
    template_name = "adicionaisPagos/list_adicionaisPagos.html"
    adicionais = AdicionaisPagos.objects.filter()
    context = {"adicionaisPagos": adicionais}
    return render(request, template_name, context)


def edit_adicionalPago(request, id_adicional):
    template_name = "adicionaisPagos/add_adicionalPago.html"
    context = {}
    adicional = get_object_or_404(AdicionaisPagos, id=id_adicional)
    if request.method == "POST":
        form = AdicionaisPagoForm(request.POST, instance=adicional)
        if form.is_valid():
            form.save()
            return redirect("adicionaisPago:list_adicionaisPagos")
    form = AdicionaisPagoForm(instance=adicional)
    context["form"] = form
    return render(request, template_name, context)


def delete_adicional(request, id_adicional):
    client = AdicionaisPagos.objects.get(id=id_adicional)
    client.delete()
    return redirect("adicionaisPago:list_adicionaisPagos")
