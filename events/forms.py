from django import forms
from .models import Evento, Inscricao


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = {'nome', 'email', 'evento_assossiado'}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu e-mail'}),
            'data_inscricao': forms.DateField(),
            'evento_assossiado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escolha o evento'}),

        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O campo email é obrigatório.")
        return email
