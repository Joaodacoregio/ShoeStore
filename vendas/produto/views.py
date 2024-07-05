import logging

from django.contrib import messages
from django.http import (HttpRequest, HttpResponse, HttpResponseNotAllowed,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ProdutoForm
from .models import Produto

logger = logging.getLogger(__name__)


def listar_produtos(request: HttpRequest) -> HttpResponse:
    produtos = Produto.objects.all()
    return render(
        request=request,
        template_name="vendas/produto/listar_produtos.html",
        context={"produtos": produtos},
    )


def criar_produto(request: HttpRequest) -> render:
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            try:
                novo_produto = Produto(
                    nome=form.cleaned_data["nome"],
                    preco=form.cleaned_data["preco"],
                    cor=form.cleaned_data["cor"],
                    tamanho=form.cleaned_data["tamanho"],
                    referencia=form.cleaned_data["referencia"],
                )
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
            finally:
                return redirect("listar_produtos")
    else:
        form = ProdutoForm()
        return render(
            request=request,
            template_name="vendas/produto/criar_produto.html",
            context={"form": form},
        )


def editar_produto(
    request: HttpRequest, produto_id: int
) -> HttpResponse | HttpResponseRedirect:
    produto = get_object_or_404(klass=Produto, id=produto_id)

    initial_data = {
        "nome": produto.nome,
        "preco": produto.preco,
        "cor": produto.cor,
        "tamanho": produto.tamanho,
        "referencia": produto.referencia,
    }

    if request.method != "POST":
        form = ProdutoForm(initial=initial_data)
        return render(
            request=request,
            template_name="vendas/produto/editar_produto.html",
            context={
                "form": form,
                "delete_url": reverse(
                    viewname="deletar_produto",
                    kwargs={"produto_id": produto_id},
                ),
            },
        )

    form = ProdutoForm(data=request.POST, initial=initial_data)

    if not form.has_changed() or not form.is_valid():
        return redirect("editar_produto", produto_id=produto_id)

    try:
        for field in form.changed_data:
            setattr(produto, field, form.cleaned_data[field])
        produto.save()
        messages.success(
            request=request,
            message="Produto editado com sucesso!",
        )
    except Exception as e:
        logger.exception(msg=e)
        messages.error(
            request=request,
            message="Erro ao editar produto",
        )
    finally:
        return redirect("editar_produto", produto_id=produto_id)


def deletar_produto(
    request: HttpRequest, produto_id: int
) -> HttpResponseRedirect | HttpResponseNotAllowed:
    produto = get_object_or_404(klass=Produto, id=produto_id)

    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])

    try:
        produto.delete()
        messages.success(
            request=request, message="Produto deletado com sucesso!"
        )
    except Exception as e:
        logger.exception(msg=e)
        messages.error(
            request=request,
            message="Erro ao deletar produto",
        )
    finally:
        return redirect("listar_produtos")


def obter_nome_produto(request: HttpRequest) -> render:
    if request.method == "GET":
        produto_id = request.GET.get("produto_id")
        try:
            produto = Produto.objects.get(id=produto_id)
            return JsonResponse({"nome_produto": produto.nome})
        except Produto.DoesNotExist:
            return JsonResponse({"error": "Produto não encontrado"}, status=404)
    else:
        return JsonResponse({"error": "Método não suportado"}, status=405)


def obter_preco_produto(request: HttpRequest) -> render:
    if request.method == "GET":
        produto_id = request.GET.get("produto_id")
        try:
            produto = Produto.objects.get(id=produto_id)
            return JsonResponse({"preco_produto": produto.preco})
        except Produto.DoesNotExist:
            return JsonResponse({"error": "Produto não encontrado"}, status=404)
    else:
        return JsonResponse({"error": "Método não suportado"}, status=405)
