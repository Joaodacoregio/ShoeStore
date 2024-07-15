from django import forms
from ..categoria.models import Category
from ..marca.models import Mark
from .models import Product

COLOR_BASIC_CHOICES = [
    ('vermelho', 'Vermelho'),
    ('azul', 'Azul'),
    ('verde', 'Verde'),
    ('amarelo', 'Amarelo'),
    ('preto', 'Preto'),
    ('branco', 'Branco'),
]


GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title", "reference", "category", "mark", "gener", "size", 
            "color", "sale_price", "img",'cost_price','profit_margin',
        ]

    title = forms.CharField(
        label="Nome do produto",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
 
 
    size = forms.DecimalField(
        label="Tamanho",
        max_digits=5,
        decimal_places=2,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'display: none;'})
    )

    color = forms.ChoiceField(
        choices=COLOR_BASIC_CHOICES,
        label='Cor',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Categoria",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    mark = forms.ModelChoiceField(
        queryset=Mark.objects.all(),
        label="Marca",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    img = forms.ImageField(
        label="Imagem",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
    reference = forms.CharField(
        label="Referencia",
        max_length=32,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

 
    gener = forms.ChoiceField(
        choices=GENERO_CHOICES,
        label='Gênero',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    sale_price = forms.DecimalField(
        label="Preço de venda",
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    profit_margin = forms.DecimalField(
        label="Margem de lucro(%)",
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    cost_price = forms.DecimalField(
        label="Preço de custo",
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
 