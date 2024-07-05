from datetime import datetime

from django.test import TestCase

from ...venda.models import ItemVenda, Venda
from ..test_data_util import (create_test_cliente1, create_test_endereco1,
                              create_test_produto1, create_test_produto2,
                              create_test_vendedor1)


class VendaTestCase(TestCase):
    def test_venda_has_many_items(self):
        venda = Venda.objects.create(
            data_venda=datetime.now().date(),
            vendedor=create_test_vendedor1(),
            cliente=create_test_cliente1(endereco=create_test_endereco1()),
            comissao=10.0,
        )

        ItemVenda.objects.create(
            venda=venda,
            produto=create_test_produto1(),
            quantidade=1,
            desconto=5.0,
        )

        ItemVenda.objects.create(
            venda=venda,
            produto=create_test_produto2(),
            quantidade=2,
            desconto=5.0,
        )

        self.assertEqual(venda.itens.count(), 2)
