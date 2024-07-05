from django.test import TestCase

from ...venda.models import ItemVenda, Venda
from ...venda.serializers import VendaWriteSerializer
from ..test_data_util import (create_test_cliente1, create_test_endereco1,
                              create_test_produto1, create_test_produto2,
                              create_test_vendedor1)


class VendaWriteSerializerTestCase(TestCase):
    def setUp(self):
        create_test_vendedor1()
        create_test_cliente1(endereco=create_test_endereco1())
        create_test_produto1()
        create_test_produto2()

        self.venda_data = {
            "vendedor": 1,
            "cliente": 1,
            "data_venda": "2000-01-15",
            "itens": [
                {
                    "produto": 1,
                    "quantidade": 1,
                    "desconto": 10.74,
                    "comissao": 5.89,
                },
                {
                    "produto": 2,
                    "quantidade": 2,
                    "desconto": 15.57,
                    "comissao": 3.65,
                },
            ],
        }

    def test_serializer_is_valid(self):
        serializer = VendaWriteSerializer(data=self.venda_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_is_not_valid(self):
        invalid_data = self.venda_data.copy()
        invalid_data["cliente"] = 99
        invalid_data["itens"][0]["produto"] = 99
        invalid_data.pop("data_venda")

        serializer = VendaWriteSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("cliente", serializer.errors)
        self.assertIn("produto", serializer.errors["itens"][0])
        self.assertIn("data_venda", serializer.errors)

    def test_serializer_create_method(self):
        serializer = VendaWriteSerializer(data=self.venda_data)
        self.assertTrue(serializer.is_valid())

        venda = serializer.save()

        self.assertIsInstance(venda, Venda)
        self.assertEqual(venda.itens.count(), 2)
        self.assertEqual(ItemVenda.objects.count(), 2)
