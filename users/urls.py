from django.urls import path, include

from events import views
from users.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register_usuario, name='register'),
]

