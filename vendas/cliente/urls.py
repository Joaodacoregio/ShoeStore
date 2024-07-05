from django.urls import path

from .views import (criar_cliente, deletar_cliente, editar_cliente,
                    listar_clientes, obter_nome_cliente)

cliente_urlpatterns = [
    path("clientes/", listar_clientes, name="listar_clientes"),
    path("clientes/criar/", criar_cliente, name="criar_cliente"),
    path(
        "clientes/editar/<int:cliente_id>/",
        editar_cliente,
        name="editar_cliente",
    ),
    path(
        "clientes/deletar/<int:cliente_id>/",
        deletar_cliente,
        name="deletar_cliente",
    ),
    path(
        "api/obter_nome_cliente/", obter_nome_cliente, name="obter_nome_cliente"
    ),
]
