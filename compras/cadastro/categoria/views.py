import logging

from .models import Category
from django.shortcuts import render
from .forms import CategoryForm
from django.contrib import messages
from django.shortcuts import  render


logger = logging.getLogger(__name__)



def cadastrar_categoria(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                nova_categoria = Category(name=form.cleaned_data["name"])
                nova_categoria.save()
                messages.success(request, "Categoria cadastrada com sucesso!")
            except Exception as e:
                logger.exception(e)
                messages.error(request, "Erro ao criar categoria!")
    else:
        form = CategoryForm()
    
    return render(
        request, 
        "compras/pages/cadastro/categoria/cadastrar_categoria.html", 
        {"form": form}
    )
