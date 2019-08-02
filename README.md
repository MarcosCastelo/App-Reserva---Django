# App Reserva

Mini Aplicação web feita em django na qual tenta simular a compra de um ingresso no cinema

## Models

Todo o banco de dados da aplicação é composto por apenas 5 entidades

```bash
class Cliente(models.Model)
class Filme(models.Model)
class Sala(models.Model)
class Poltrona(models.Model)
class Sessao(models.Model)
```

## Views

São 5 views principais:
- index: lista os filmes em cartaz hoje
- programação: lista os filmes em cartas dos demais dias
- detail: informa as poltronas disponiveis de uma determinada sessão
- reserva: reserva uma poltrona ao preencher um nome e escolher uma poltrona

## Urls
 - "/" : index
 - "/<str:data>" : programacao do dia dd-mm-yy
 - "/detail/<int:sessao_id>" : detalhe de uma sessão
 - "/detail/<int:sessao_id>/reserva" : url para reservar que redireciona para detail 
