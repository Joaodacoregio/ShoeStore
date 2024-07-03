from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request)->HttpResponse:
    return render(request,"ShoeStore/pages/home.html")

def contato(request)->HttpResponse:
    return render(request,"ShoeStore/contato.html")


