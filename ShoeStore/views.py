from django.shortcuts import render
from django.http import HttpResponse

def home(request)->HttpResponse:
    return HttpResponse("HOME")

def test(request)->HttpResponse:
    return HttpResponse("test")


