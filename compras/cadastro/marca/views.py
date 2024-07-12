import logging

from .models import Mark
from django.shortcuts import render
from .forms import MarcaForm
from django.contrib import messages
from django.shortcuts import  render


logger = logging.getLogger(__name__)


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
