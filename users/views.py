from django.shortcuts import render

from events.models import Inscricao, Evento


# Create your views here.
def dashboard(request):
    inscricao = Inscricao.objects.filter(usuario=request.user)
    eventos = Evento.objects.filter(organizador=request.user)

    return render(request, "users/dashboard.html", {'inscricao': inscricao, 'eventos': eventos})
