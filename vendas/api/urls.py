from django.urls import path

from .views import ProdutoDetalheView, criar_venda

api_urlpatterns = [
    path(
        "api/produtos/<int:id>",
        ProdutoDetalheView.as_view(),
        name="produto_detalhe",
    ),
    path(
        "api/vendas/",
        criar_venda,
        name="criar_venda",
    ),
]
