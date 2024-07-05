from django.contrib import messages
from django.http import HttpRequest, JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, ParseError

from ..produto.models import Produto
from ..produto.serializers import ProdutoReadSerializer
from ..venda.serializers import VendaWriteSerializer


class ProdutoDetalheView(generics.RetrieveAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoReadSerializer
    lookup_field = "id"


@api_view(["POST"])
def criar_venda(request: HttpRequest):
    try:
        serializer = VendaWriteSerializer(data=JSONParser().parse(request))

    except ParseError:
        messages.error(request=request, message="Erro ao finalizar a venda!")
        return JsonResponse({"detail": "Invalid JSON"}, status=400)

    if not serializer.is_valid():
        messages.error(request=request, message="Erro ao finalizar a venda!")
        return JsonResponse(serializer.errors, status=400)

    messages.success(request=request, message="Venda concluida com sucesso!")
    serializer.save()
    return JsonResponse(serializer.data, status=201)
