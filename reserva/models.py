from django.db import models
from reserva.utils import *


class Cliente(models.Model):
    nome = models.CharField(max_length=50)


class Filme(models.Model):
    nome = models.CharField(max_length=50)
    duracao = models.IntegerField
    classificacao = models.IntegerField(
        choices=CLASSIFICACAO_INDICATIVA_CHOICES, default=1)
    trailer = models.CharField(max_length=35)


class Sala(models.Model):
    nome = models.CharField(max_length=20)


class Poltrona(models.Model):
    posicao = models.CharField(max_length=2)
    tipo = models.IntegerField(choices=POLTRONAS_CHOICES, default=1)
    cliente = models.ForeignKey(
        Cliente, related_name='poltrona_cliente', on_delete='CASCADE', null=True)
    sala = models.ForeignKey(
        Sala, related_name='poltrona_sala', on_delete='CASCADE')


class Sessao(models.Model):
    dublado = models.BooleanField(default=True)
    pub_data = models.DateField()
    horario = models.TimeField()
    tecnologia = models.IntegerField(choices=TECNOLOGIAS_CHOICES, default=1)
    sala = models.ForeignKey(
        Sala, related_name='sessao_sala', on_delete='CASCADE')
    filme = models.ForeignKey(
        Filme, related_name='sessao_filme', on_delete='CASCADE')
