from django import forms


class ProdutoForm(forms.Form):
    nome = forms.CharField(
        label="Nome do Produto",
        max_length=255,
        required=True,
    )
    preco = forms.DecimalField(
        label="Preço do Produto",
        min_value=0,
        decimal_places=2,
        required=True,
    )
    cor = forms.CharField(
        label="Cor do Produto",
        max_length=255,
        required=True,
    )
    tamanho = forms.CharField(
        label="Tamanho do Produto",
        max_length=255,
        required=True,
    )
    referencia = forms.CharField(
        label="Referência do Produto",
        max_length=255,
        required=False,
    )
