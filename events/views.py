from django.shortcuts import render, get_object_or_404, redirect

from events.models import Evento
from events.forms import *


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


def inscricao_evento(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_eventos')
    else:
        form = InscricaoForm()
    return render(request, 'form_inscricao.html', {'form': form})
