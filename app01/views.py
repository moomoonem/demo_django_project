from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, "index.html")


def sign_up(request):
    return render(request, "sign_up.html")

def login(request):
    return render(request, "login.html")
