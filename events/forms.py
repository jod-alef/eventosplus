from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class RegistroUsuario(UserCreationForm):
    nome_completo = forms.CharField(max_length=160)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['nome_completo', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O campo email é obrigatório.")
        return email


class EdicaoUsuario(forms.ModelForm):
    nome_completo = forms.CharField(max_length=160)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['nome_completo', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O campo email é obrigatório.")
        return email
