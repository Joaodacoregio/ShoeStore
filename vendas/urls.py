from django.urls import path

from .api.urls import api_urlpatterns
from .cliente.urls import cliente_urlpatterns
from .produto.urls import produto_urlpatterns
from .venda.urls import venda_urlpatterns
from .vendedor.urls import vendedor_urlpatterns
from .views import home

common_urls = [path("", home, name="home")]

# NOTE: incluir urlpatterns dos submodulos aqui para registralos no app
INCLUDE_URLS = (
    common_urls,
    cliente_urlpatterns,
    produto_urlpatterns,
    venda_urlpatterns,
    vendedor_urlpatterns,
    api_urlpatterns,
)

joined_urls = []
for urlpattern_list in INCLUDE_URLS:
    joined_urls.extend(urlpattern_list)

urlpatterns = joined_urls
