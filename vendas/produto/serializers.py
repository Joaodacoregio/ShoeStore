from rest_framework import serializers

from .models import Produto


class ProdutoReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
