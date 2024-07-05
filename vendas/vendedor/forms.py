from django import forms
from .models import Vendedor




class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = [
            "id",
            "nome",
            "cpf",
            "data_nascimento",
            "matricula",
            "data_contratacao",
        ]
        widgets = {
            "data_nascimento": forms.DateInput(
                attrs={"type": "date", "class": "form-control medium-input"}
            ),
            "data_contratacao": forms.DateInput(
                attrs={"type": "date", "class": "form-control medium-input"}
            ),
            "cpf": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "pattern": r"\d{11}",
                    "title": "Formato inválido. Deve conter 11 dígitos.",
                }
            ),
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "matricula": forms.TextInput(attrs={"class": "form-control"}),
        }