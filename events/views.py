from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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


@login_required()
def inscricao_de_evento(request):
    if request.method == 'POST':
        form = InscricaoEvento(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_eventos')
    else:
        form = InscricaoEvento()
    return render(request, 'form_evento.html', {'form': form})


@login_required()
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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {'error': 'Credenciais Inválidas'})
    return render(request, 'login.html')


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
