from django.http import HttpRequest
from django.shortcuts import render

from ..cliente.models import Cliente
from ..produto.models import Produto
from ..vendedor.models import Vendedor
from .models import Venda


def nova_venda(request: HttpRequest) -> render:
    return render(request, "vendas/venda/nova_venda.html")


def listar_vendas(request: HttpRequest):
    vendas = Venda.objects.all().order_by("-data_venda")
    return render(
        request=request,
        template_name="vendas/venda/listar_vendas.html",
        context={"vendas": vendas},
    )


def selecionar_cliente(request: HttpRequest) -> render:
    clientes = Cliente.objects.all()
    return render(
        request,
        "vendas/cliente/selecionar_cliente.html",
        {"clientes": clientes},
    )


def selecionar_vendedor(request: HttpRequest) -> render:
    vendedores = Vendedor.objects.all()
    return render(
        request,
        "vendas/vendedor/selecionar_vendedor.html",
        {"vendedores": vendedores},
    )


def selecionar_produto(request: HttpRequest) -> render:
    produtos = Produto.objects.all()
    return render(
        request,
        "vendas/produto/selecionar_produto.html",
        {"produtos": produtos},
    )
