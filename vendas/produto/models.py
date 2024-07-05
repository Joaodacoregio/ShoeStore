from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False)
    preco = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, null=False
    )
    cor = models.CharField(max_length=255, null=False)
    tamanho = models.CharField(max_length=255, null=False)
    referencia = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return f"id: {self.id}, nome: {self.nome}, preco: {self.preco}, \
            cor: {self.cor}, tamanho: {self.tamanho}"
