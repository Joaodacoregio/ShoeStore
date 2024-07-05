from rest_framework import serializers

from .models import ItemVenda, Venda


class ItemVendaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        exclude = ["venda"]


class VendaWriteSerializer(serializers.ModelSerializer):
    itens = ItemVendaWriteSerializer(many=True)

    class Meta:
        model = Venda
        fields = "__all__"

    def create(self, validated_data):
        items_data = validated_data.pop("itens")
        venda = Venda.objects.create(**validated_data)
        for item_data in items_data:
            ItemVenda.objects.create(venda=venda, **item_data)
        return venda
