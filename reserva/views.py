from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.views import generic
import datetime
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
