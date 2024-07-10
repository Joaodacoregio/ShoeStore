from django.shortcuts import render
from tests.compras.products.factory import make_product

# Create your views here.
def compras_home(request):
    return render(request,"compras/pages/compras_home.html" , context={
        'products':[make_product for _ in range(10)],
    })  



def produto(request,id):
    return render(request,"compras/pages/product-view.html")  


def cadastrar_marca(request):
    return render(request,"compras/pages/cadastrar_marca.html")