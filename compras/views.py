import logging

from django.shortcuts import render
from tests.compras.products.factory import make_product
from .forms import CategoryForm,MarcaForm
from .models import Mark
from django.contrib import messages
from django.shortcuts import  render


logger = logging.getLogger(__name__)

# Create your views here.
def compras_home(request):
    return render(request,"compras/pages/compras_home.html" , context={
        'products':[make_product for _ in range(10)],
    })  



def produto(request,id):
    return render(request,"compras/pages/product-view.html")  


def cadastrar_marca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            try:
                nova_marca = Mark(name=form.cleaned_data["name"])
                nova_marca.save()
                messages.success(request, "Marca cadastrada com sucesso!")
            except Exception as e:
                logger.exception(e)
                messages.error(request, "Erro ao criar marca!")
    else:
        form = MarcaForm()
    
    return render(
        request, 
        "compras/pages/cadastrar_marca.html", 
        {"form": form}
    )


def cadastrar_categoria(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                nova_marca = Mark(name=form.cleaned_data["name"])
                nova_marca.save()
                messages.success(request, "Categoria cadastrada com sucesso!")
            except Exception as e:
                logger.exception(e)
                messages.error(request, "Erro ao criar categoria!")
    else:
        form = CategoryForm()
    
    return render(
        request, 
        "compras/pages/cadastrar_categoria.html", 
        {"form": form}
    )