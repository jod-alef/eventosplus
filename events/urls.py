from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('list_eventos/', views.list_eventos, name='list_eventos'),
    path('list_detalhes_eventos/<int:evento_id>', views.list_detalhes_eventos, name='list_detalhes_eventos'),
    path('form_inscricao/', views.inscricao_evento, name='inscricao_evento'),
    path('form_evento/', views.inscricao_de_evento, name='inscricao_de_evento'),
    path('editar_evento/<int:evento_id>', views.editar_evento, name='editar_evento'),
    path('user_login/', views.user_login, name='login'),
    path('user_logout/', views.user_logout, name='logout'),
]