import logging

  
from .cadastro.produto.models import Product
from django.shortcuts import get_list_or_404
from django.shortcuts import render
 
 


logger = logging.getLogger(__name__)

# Create your views here.
def compras_home(request):
    products = Product.objects.all().order_by("-id")
    return render(request,"compras/pages/compras_home.html" , context={
        'products':products,
    })  



def produto(request,id):
    return render(request,"compras/pages/product-view.html")  





#filter
def filtrar_marca(request,marca_id):
    products = get_list_or_404(
        Product.objects.filter(mark__id=marca_id).order_by("-id")
    )


    return render(request,"compras/pages/compras_home.html" , context={
        'products':products,
        "title": f"{products[0].mark.name}|"
    })  


def filtrar_categoria(request,categoria_id):
    products = get_list_or_404(
        Product.objects.filter(category__id=categoria_id).order_by("-id")
    )
 
    
    return render(request,"compras/pages/compras_home.html" , context={
        'products':products,
        "title": f"{products[0].category.name}|",
    })  

def filtrar_genero(request,genero):
    products = get_list_or_404(Product.objects.filter(gener=genero).order_by("-id"))

    return render(request,"compras/pages/compras_home.html" , context={
        'products':products,
        "title":f"{products[0].gener}|"
    })  



