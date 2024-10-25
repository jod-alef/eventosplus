from django.db import models


# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_final = models.DateField()
    descricao = models.TextField()
    local = models.CharField(max_length=50)

    def __str__(self):
        return f"Evento: {self.nome} - Inicio: {self.data_inicio} - Final: {self.data_final} - Descricao: {self.descricao} - Local: {self.local}"
