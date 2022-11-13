from django.shortcuts import render
from .models import Correspondencia
from django.contrib.auth.models import User


def home(request):
    correspondencias = Correspondencia.objects.all()
    users = User.objects.all()
    return render(request,'app/home.html', {"correspondencias":correspondencias, "users":users}) 
