from django import forms
from ..categoria.models import Category
from ..marca.models import Mark
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title", "reference", "category", "mark", "gener", "size", 
            "color", "title_slug", "price", "img"
        ]

    title = forms.CharField(
        label="Nome do produto",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    title_slug = forms.SlugField(
        label="Nome do produto slug",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    price = forms.DecimalField(
        label="Preço",
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    size = forms.DecimalField(
        label="Tamanho",
        max_digits=5,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    color = forms.CharField(
        label="Cor",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
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

    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    ]
    gener = forms.ChoiceField(
        choices=GENERO_CHOICES,
        label='Gênero',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
