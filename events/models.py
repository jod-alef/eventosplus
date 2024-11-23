from django.db import models
from django.contrib.auth.models import User, Group, Permission, AbstractUser
from django.contrib.contenttypes.models import ContentType


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_final = models.DateField()
    descricao = models.TextField()
    local = models.CharField(max_length=50)
    organizador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Evento: {self.nome} - Inicio: {self.data_inicio} - Final: {self.data_final} - Descricao: {self.descricao} - Local: {self.local} - Organizador: {self.organizador}"


class Inscricao(models.Model):
    data_inscricao = models.DateField(auto_now_add=True)
    detalhes_evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Usuario: {self.usuario} - Nome: {self.usuario.first_name} -  Data de Inscrição: {self.data_inscricao} - Detalhes do Evento: {self.detalhes_evento}"

