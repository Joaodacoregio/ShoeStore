from django.urls import path

from .views import (listar_vendas, nova_venda, selecionar_cliente,
                    selecionar_produto, selecionar_vendedor)

venda_urlpatterns = [
    path("vendas/", listar_vendas, name="listar_vendas"),
    path("vendas/nova-venda", nova_venda, name="nova_venda"),
    path(
        "vendas/selecionar_cliente",
        selecionar_cliente,
        name="selecionar_cliente",
    ),
    path(
        "vendas/selecionar_vendedor",
        selecionar_vendedor,
        name="selecionar_vendedor",
    ),
    path(
        "vendas/selecionar_produto",
        selecionar_produto,
        name="selecionar_produto",
    ),
]
