from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.views import generic
from .models import *
from .utils import *


class IndexView(generic.ListView):
    template_name = 'reserva/index.html'
    context_object_name = 'sessao_list'

    def get_queryset(self):
        sessoes = list(Sessao.objects.filter(pub_data__range=(HOJE, FAIXA_DE_TEMPO)))
        programacao = list()
        for sessao in sessoes:
            programacao.append(Sessao.objects.filter(filme = sessao.filme))
            sessoes.remove(sessao)
        return programacao
