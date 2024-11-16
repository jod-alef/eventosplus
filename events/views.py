import csv
from datetime import datetime
from functools import wraps

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from events.forms import *
from users.views import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def custom_group_required(required_groups):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if any(group in user.groups.values_list('name', flat=True) for group in required_groups):
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied

        return wrapper

    return decorator


def list_eventos(request):
    query = Evento.objects.all()

    return render(request, 'list_eventos.html', {'eventos': query})


@custom_group_required(['Organizadores'])
def list_eventos_organizador(request):
    query = Evento.objects.filter(organizador=request.user)

    return render(request, 'list_eventos_organizador.html', {'eventos': query})


def list_detalhes_eventos(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    return render(request, 'list_detalhes_eventos.html', {'evento': evento})


@login_required()
def inscricao_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    # Verifica se o usuário já está inscrito no evento
    if Inscricao.objects.filter(usuario=request.user, detalhes_evento=evento).exists():
        # Adiciona uma mensagem de erro para informar que o usuário já está inscrito
        messages.error(request, 'Você já está inscrito neste evento.')
        return redirect('dashboard')  # Redireciona para a lista de eventos inscritos

    if request.method == 'POST':
        inscricao = Inscricao.objects.create(
            usuario=request.user,
            data_inscricao=datetime.now(),
            detalhes_evento=evento,
        )
        inscricao.save()
        messages.success(request, 'Inscrição realizada com sucesso!')
        return redirect('dashboard')

    return render(request, 'list_eventos_inscritos.html', {'evento': evento})


@login_required()
def list_eventos_inscritos(request):
    inscricao = Inscricao.objects.filter(usuario=request.user)
    return render(request, 'list_eventos_inscritos.html', {'inscricao': inscricao})


@login_required()
def apagar_inscricao(request, inscricao_id):
    inscricao = get_object_or_404(Inscricao, id=inscricao_id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('dashboard')
    return render(request, 'list_eventos_inscritos.html', {'inscricao': inscricao})


@login_required()
def list_eventos_organizador(request):
    query = Evento.objects.filter(organizador=request.user)

    return render(request, 'list_eventos_organizador.html', {'eventos': query})


@custom_group_required(['Organizadores'])
def inscricao_de_evento(request):
    if request.method == 'POST':
        form = InscricaoEvento(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user
            evento.save()
            return redirect('list_eventos_organizador')
    else:
        form = InscricaoEvento()
    return render(request, 'form_evento.html', {'form': form})


@custom_group_required(['Organizadores'])
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        form = InscricaoEvento(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('list_eventos')
    else:
        form = InscricaoEvento(instance=evento)
    return render(request, 'form_evento.html', {'form': form, 'evento': evento})


@custom_group_required(['Organizadores'])
def listar_participantes_evento(request):
    inscricoes = Inscricao.objects.filter(detalhes_evento__organizador=request.user)

    return render(request, 'listar_participantes.html', {'inscricoes': inscricoes})


@custom_group_required(['Organizadores'])
def exportar_inscricoes_csv(request):
    lista_inscricoes = Inscricao.objects.filter(detalhes_evento__organizador=request.user)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inscricoes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome do Evento', 'Nome', 'Sobrenome', 'Data de Inscrição', 'Usuário'])

    for inscricao in lista_inscricoes:
        writer.writerow([inscricao.detalhes_evento.nome, inscricao.usuario.first_name, inscricao.usuario.last_name,
                         inscricao.data_inscricao, inscricao.usuario.username])

    return response
