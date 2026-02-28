from django.shortcuts import render, redirect
from .models import User


def user_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        User.objects.create(name=name, email=email)
        return redirect("login")

    return render(request, "form.html")


from django.contrib import messages

def login_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        user = User.objects.filter(name=name, email=email).first()

        if user:
            return render(request, "success.html", {"user": user})
        else:
            messages.error(request, "User not found. Please check your details.")
            return redirect("login")   # 👈 redirect is key

    return render(request, "login.html")