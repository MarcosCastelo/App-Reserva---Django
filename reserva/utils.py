import datetime

HOJE = datetime.date.today()
FAIXA_DE_TEMPO = HOJE + datetime.timedelta(days=7)

CLASSIFICACAO_INDICATIVA_CHOICES = (
    (1, "L"),
    (2, "10"),
    (3, "12"),
    (4, "14"),
    (5, "16"),
    (6, "18")
)

POLTRONAS_CHOICES = (
    (1, "Simples"),
    (2, "Namoradeira"),
    (3, "Cadeirante"),
    (4, "Acompanhante"),
)

TECNOLOGIAS_CHOICES = (
    (1, '2D'),
    (2, '3D'),
)


