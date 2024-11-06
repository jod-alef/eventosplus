from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_eventos/', views.list_eventos, name='list_eventos'),
    path('list_eventos_organizador/', views.list_eventos_organizador, name='list_eventos_organizador'),
    path('list_detalhes_eventos/<int:evento_id>', views.list_detalhes_eventos, name='list_detalhes_eventos'),
    path('inscricao_evento/<int:evento_id>', views.inscricao_evento, name='inscricao_evento'),
    path('list_eventos_inscritos/', views.list_eventos_inscritos, name='list_eventos_inscritos'),
    path('form_evento/', views.inscricao_de_evento, name='inscricao_de_evento'),
    path('editar_evento/<int:evento_id>', views.editar_evento, name='editar_evento'),
    path('apagar_inscricao/<int:inscricao_id>', views.apagar_inscricao, name='apagar_inscricao'),

]