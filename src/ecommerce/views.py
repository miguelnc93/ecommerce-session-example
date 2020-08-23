from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

def home_page(request):
    context = {
        "title":"Hello world"
    }
    return render(request, "home_page.html",context)

def about_page(request):
    context = {
        "title":"About"
    }
    return render(request, "home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    ctx = {
        "contact_form": contact_form,
        "title": "Example of title"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST['fullname'])
    #     print(request.POST['email'])
    #     print(request.POST['content'])

    return render(request, "contact.html",ctx)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("user logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            context["form"] = LoginForm() #limpiar formulario
            return redirect("home")
        else:
            print("error")

    return render(request,"auth/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('home')
    
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, password)
        print(new_user)
    return render(request,"auth/register.html", context)