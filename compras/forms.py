from django import forms


class MarcaForm(forms.Form):
    name = forms.CharField(
        label="Nome da marca",
        max_length=255,
        required=True,
    )


class CategoryForm(forms.Form):
    name = forms.CharField(
        label="Nome da categoria",
        max_length=255,
        required=True,
    )