from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    data_nascimento = models.DateField(null=False)

    def __str__(self) -> str:
        return f"id: {self.id}, nome: {self.nome}"

    class Meta:
        abstract = True
