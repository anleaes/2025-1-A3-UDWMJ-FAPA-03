from django.shortcuts import render, redirect

from apps.accounts.forms import UserForm


# Create your views here.
def add_user(request):
    template_name = "accounts/add_user.html"
    context = {}
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f = form.save()
            return redirect("accounts:user_login")
        else:
            return redirect("accounts:add_user")
    form = UserForm()
    context["form"] = form
    return render(request, template_name, context)
