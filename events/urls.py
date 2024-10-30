from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('list_eventos/', views.list_eventos, name='list_eventos'),
    path('list_detalhes_eventos/<int:evento_id>', views.list_detalhes_eventos, name='list_detalhes_eventos'),
]