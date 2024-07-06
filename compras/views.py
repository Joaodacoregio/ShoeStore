from django.shortcuts import render

# Create your views here.
def compras_home(request):
    return render(request,"compras/pages/compras_home.html")  

