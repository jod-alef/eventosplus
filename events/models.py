from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_final = models.DateField()
    descricao = models.TextField()
    local = models.CharField(max_length=50)
    organizador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Evento: {self.nome} - Inicio: {self.data_inicio} - Final: {self.data_final} - Descricao: {self.descricao} - Local: {self.local}"


class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_inscricao = models.DateField(auto_now_add=True)
    evento_assossiado = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inscricao: {self.nome} - Email: {self.email}"
