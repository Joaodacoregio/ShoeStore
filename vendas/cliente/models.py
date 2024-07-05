from django.db import models

from ..models import Pessoa


class Endereco(models.Model):
    rua = models.CharField(max_length=255, null=False)
    numero = models.CharField(max_length=10, null=False)
    cidade = models.CharField(max_length=255, null=False)
    estado = models.CharField(max_length=2, null=False)
    cep = models.CharField(max_length=8, null=False)

    def __str__(self) -> str:
        return f"id: {self.id}, rua: {self.rua}, cidade: {self.cidade}, estado: {self.estado}"


class Cliente(Pessoa):
    email = models.CharField(max_length=255, null=True)
    telefone = models.CharField(max_length=20, null=True)
    endereco = models.OneToOneField(to=Endereco, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{super().__str__()}, email: {self.email}"
