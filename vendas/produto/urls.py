from django.urls import path

from .views import (criar_produto, deletar_produto, editar_produto,
                    listar_produtos, obter_nome_produto, obter_preco_produto)

produto_urlpatterns = [
    path("produtos/", listar_produtos, name="listar_produtos"),
    path("produtos/criar", criar_produto, name="criar_produto"),
    path("produtos/<int:produto_id>/", editar_produto, name="editar_produto"),
    path(
        "produtos/<int:produto_id>/deletar",
        deletar_produto,
        name="deletar_produto",
    ),
    path(
        "api/obter_nome_produto/", obter_nome_produto, name="obter_nome_produto"
    ),
    path(
        "api/obter_preco_produto/",
        obter_preco_produto,
        name="obter_preco_produto",
    ),
]
