from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def accedi(request):
    return render(request, 'login.html', {})


def registrati(request):
    return render(request, 'register.html', {})