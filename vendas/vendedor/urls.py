from django.urls import path

from .views import (criar_vendedor, deletar_vendedor, editar_vendedor,
                    listar_vendedores, obter_nome_vendedor)

vendedor_urlpatterns = [
    path("vendedores/", listar_vendedores, name="listar_vendedores"),
    path(
        "vendedores/criar/", criar_vendedor, name="criar_vendedor"
    ),  # Criar vendedor
    path(
        "vendedores/editar/<int:vendedor_id>/",
        editar_vendedor,
        name="editar_vendedor",
    ),  # Editar vendedor
    path(
        "vendedores/deletar/<int:vendedor_id>/",
        deletar_vendedor,
        name="deletar_vendedor",
    ),
    path(
        "api/obter_nome_vendedor/",
        obter_nome_vendedor,
        name="obter_nome_vendedor",
    ),
]
