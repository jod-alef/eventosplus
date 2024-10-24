from django.db import models

# Create your models here.

class Evento(models.Model):
    nome_evento = models.CharField(max_length=100)
    data_evento = models.DateField()
    data_final = models.DateField()
    descricao_evento = models.TextField()
    local_evento = models.CharField(max_length=100)

    def __str__(self):
        return f"Evento: {self.nome_evento} - Inicio: {self.data_evento} - Final: {self.data_final} - Descricao: {self.descricao_evento} - Local: {self.local_evento}"
