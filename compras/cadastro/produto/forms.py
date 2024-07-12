from django import forms
from ..categoria.models import Category
from ..marca.models import Mark
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # Certifique-se de que o modelo esteja corretamente importado
        fields = ['title', 'title_slug', 'price', 'size', 'color', 'category', 'mark', 'img',
                  'reference',"gener"]
    title = forms.CharField(
        label="Nome do produto",
        max_length=255,
        required=True
    )
    title_slug = forms.SlugField(
        label="Nome do produto slug",
        max_length=255,  # Corrigido: max_lenght para max_length
        required=True
    )
    price = forms.DecimalField(
        label="Preço",
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput()
    )
    size = forms.DecimalField(
        label="Tamanho",
        max_digits=5,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput()
    )
    color = forms.CharField(
        label="Cor",
        max_length=255,  # Corrigido: max_lenght para max_length
        required=True,
        widget=forms.TextInput()
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),  # Supondo que a categoria seja um modelo relacionado
        label="Categoria"
    )
    mark = forms.ModelChoiceField(
        queryset=Mark.objects.all(),  # Supondo que a marca seja um modelo relacionado
        label="Marca"
    )
    img = forms.ImageField(
        label="Imagem",
        required=False,
        widget=forms.ClearableFileInput()
    )
    reference = forms.CharField(
        max_length=32,
        required=True
    )

    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    ]
    gener = forms.ChoiceField(choices=GENERO_CHOICES, label='Gênero')

 
