import logging


from .forms import ProductForm
from django.shortcuts import render
from django.contrib import messages
 



 

logger = logging.getLogger(__name__)


def cadastrar_produto(request) -> render:
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                novo_produto = form.save()  # Não salva ainda no banco
                novo_produto.save()
                messages.success(
                    request=request,
                    message="Produto criado com sucesso!",
                )
            except Exception as e:
                logger.exception(msg=e)
                messages.error(
                    request=request,
                    message="Erro ao criar produto",
                )
    else:
        form = ProductForm()
    
    return render(
        request=request,
        template_name="compras/pages/cadastro/cadastrar_produto.html",
        context={"form": form},
    )

