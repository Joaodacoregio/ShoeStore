from django import forms
from .models import Cliente,Endereco




class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = [
            "rua",
            "cidade",
            "estado",
            "cep",
        ]
        widgets = {
            "rua": forms.TextInput(
                attrs={"class": "form-control medium-input"}
            ),
            "cidade": forms.TextInput(
                attrs={"class": "form-control medium-input"}
            ),
            "estado": forms.TextInput(
                attrs={"class": "form-control medium-input"}
            ),
            "cep": forms.TextInput(
                attrs={
                    "class": "form-control medium-input",
                    "pattern": r"\d{8}",  # Supondo que o CEP tenha 8 dígitos
                    "title": "Formato inválido. Deve conter 8 dígitos.",
                }
            ),
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "cpf", "data_nascimento", "email", "telefone"]
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control large-input"}
            ),
            "cpf": forms.TextInput(
                attrs={
                    "class": "form-control medium-input",
                    "pattern": r"\d{11}",
                    "title": "Formato inválido. Deve conter 11 dígitos.",
                }
            ),
            "data_nascimento": forms.DateInput(
                attrs={"type": "date", "class": "form-control medium-input"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control large-input"}
            ),
            "telefone": forms.TextInput(
                attrs={
                    "class": "form-control medium-input",
                    "pattern": r"\d{8,15}",  # Ajustado para um formato de telefone mais comum
                    "title": "Formato inválido. Deve conter entre 8 e 15 dígitos.",
                }
            ),
        }
