from django import forms



class CategoryForm(forms.Form):
    name = forms.CharField(
        label="Nome da categoria",
        max_length=255,
        required=True,
    )