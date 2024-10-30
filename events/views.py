from django.shortcuts import render, get_object_or_404

from events.models import Evento


# Create your views here.
def index(request):
    return render(request, 'index.html')


def list_eventos(request):
    query = Evento.objects.all()
    nome = request.GET.get('nome')
    descricao = request.GET.get('descricao')

    return render(request, 'list_eventos.html', {'eventos': query})


def list_detalhes_eventos(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    return render(request, 'list_detalhes_eventos.html', {'evento': evento})
