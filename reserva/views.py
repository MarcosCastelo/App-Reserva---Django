from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views import generic
import datetime
from django.urls import reverse
from .models import *
from .utils import * 

def programacao(request, data):
    template_name = 'reserva/index.html'
    try:
        data = datetime.datetime.strptime(data, "%d-%m-%Y")
        data = data.date()
        sessoes = list(Sessao.objects.filter(pub_data=data))
        filmes = list()
        programacao = list()
        for sessao in sessoes:
            filme = Filme.objects.get(sessao_filme = sessao)
            filmes.append(filme)
            programacao.append(sessao)

        filmes = list(set(filmes))
            
        return render(request, template_name, {
            'filmes' : filmes,
            'programacao' : programacao
        })

    except:    
        sessoes = list(Sessao.objects.filter(pub_data=HOJE))
        filmes = list()
        programacao = list()
        for sessao in sessoes:
            filme = Filme.objects.get(sessao_filme = sessao)
            filmes.append(filme)
            programacao.append(sessao)

        filmes = list(set(filmes))
            
        return render(request, template_name, {
            'filmes' : filmes,
            'programacao' : programacao
        })


def index(request):
    template_name = 'reserva/index.html'
    sessoes = list(Sessao.objects.filter(pub_data=HOJE))
    filmes = list()
    programacao = list()
    for sessao in sessoes:
        filme = Filme.objects.get(sessao_filme = sessao)
        filmes.append(filme)
        programacao.append(sessao)

    filmes = list(set(filmes))
        
    return render(request, template_name, {
        'filmes' : filmes,
        'programacao' : programacao
    })


def detail(request, sessao_id):
    template_name = 'reserva/reserva.html'
    #try:
    sessao = Sessao.objects.get(pk=sessao_id)
    poltronas = list()
    sala = sessao.sala
    poltronas_sessao = sessao.poltrona_sessao.all()
    for i in range(sala.fileiras):
        fileiras = list()
        for j in range(sala.colunas):
            fileiras.append(poltronas_sessao[j + (i * sala.colunas)])
        poltronas.append(fileiras)

    filme = sessao.filme
    return render(request, template_name, {
        'filme' : filme,
        'sessao' : sessao,
        'poltronas' : poltronas,
    })
'''
    except:
        return HttpResponse("Sessao não encontrada!")
'''

def reserva(request, sessao_id):
    sessao = get_object_or_404(Sessao, pk=sessao_id)
    if request.POST['nome'] != None and request.POST['nome'] != '': 
        print(type(request.POST['nome']))
        cliente = Cliente(nome=request.POST['nome'])
        cliente.save()
        poltrona_id = request.POST['poltrona_id']
        if poltrona_id is not None:
            poltrona = get_object_or_404(Poltrona, pk=poltrona_id)
            poltrona.cliente = cliente
            poltrona.save()
            return HttpResponseRedirect(reverse('detail', args=(sessao.id,)))
    return HttpResponseRedirect(reverse('detail', args=(sessao.id,)))