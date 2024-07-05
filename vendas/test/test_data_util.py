from datetime import datetime

from ..cliente.models import Cliente, Endereco
from ..produto.models import Produto
from ..vendedor.models import Vendedor


def create_test_vendedor1() -> Vendedor:
    return Vendedor.objects.create(
        nome="Vendedor 1",
        cpf="12345678900",
        data_nascimento=datetime.now().date(),
        matricula="MAT123",
        data_contratacao=datetime.now().date(),
    )


def create_test_endereco1() -> Endereco:
    return Endereco.objects.create(
        rua="Rua teste",
        numero="123",
        cidade="Teste",
        estado="TT",
        cep="12345678",
    )


def create_test_cliente1(endereco: Endereco) -> Cliente:
    return Cliente.objects.create(
        nome="Cliente 1",
        cpf="12345678900",
        data_nascimento=datetime.now().date(),
        email="teste@teste.com",
        telefone="11912345678",
        endereco=endereco,
    )


def create_test_produto1() -> Produto:
    return Produto.objects.create(
        nome="Produto 1",
        preco=10.00,
        cor="Preto",
        tamanho="P",
    )


def create_test_produto2() -> Produto:
    return Produto.objects.create(
        nome="Produto 2",
        preco=20.00,
        cor="Branco",
        tamanho="M",
    )
