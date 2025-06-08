from django.shortcuts import redirect, render

from apps.personal.forms import PersonalForm


# Create your views here.
def create_personal(request):
    template_name = "cliente/cadastroPersonal.html"
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
