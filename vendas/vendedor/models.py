from django.db import models

from ..models import Pessoa


class Vendedor(Pessoa):
    matricula = models.CharField(max_length=255, null=False, unique=True)
    data_contratacao = models.DateField(null=False)

    def __str__(self) -> str:
        return f"{super().__str__()}, matricula: {self.matricula}"
