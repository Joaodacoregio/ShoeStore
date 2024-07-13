import logging


from .forms import ProductForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import Http404,HttpRequest



 

logger = logging.getLogger(__name__)

#Cadastra o produto
def cadastrar_produto(request:HttpRequest) -> render:
 
    #TODO: Fazer o tratamento de erros pela sessão
    produto_data_form = request.session.get("produto_data_form",None)
    form = ProductForm(produto_data_form)
    
    return render(
        request=request,
        template_name="compras/pages/cadastro/produto/cadastrar_produto.html",
        context={"form": form},
    )

#Envia o produto  
def enviar_produto(request:HttpRequest)->redirect:
    #Navegador faz GET por padrão
    if not request.POST:
        raise Http404()
    
    #Armazena na sessão o POST para tratamento de erros 
    POST = request.POST
    request.session["produto_form_data"]=POST

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
    return redirect("compras:cadastrar_produto")
    