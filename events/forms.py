from django import forms
from .models import Evento, Inscricao


class InscricaoEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'data_inicio', 'data_final', 'descricao', 'local']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do evento'}),
            'data_inicio': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'type': 'date'}),
            'data_final': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'type': 'date'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o local do evento'}),
        }


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome', 'email', 'evento_assossiado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu e-mail'}),
            'evento_assossiado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escolha o evento'}),

        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O campo email é obrigatório.")
        return email


