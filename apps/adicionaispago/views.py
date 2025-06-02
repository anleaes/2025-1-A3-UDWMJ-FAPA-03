from django.shortcuts import render, redirect
from .form import AdicionaisPagoForm

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

            return redirect("core:home")  # mudar depois para listar os adicionais

    form = AdicionaisPagoForm()
    context["form"] = form
    return render(request, template_name, context)
