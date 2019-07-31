# Generated by Django 2.2 on 2019-07-31 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('classificacao', models.IntegerField(choices=[(1, 'L'), (2, '10'), (3, '12'), (4, '14'), (5, '16'), (6, '18')], default=1)),
                ('trailer', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('tecnologia', models.IntegerField(choices=[(1, '2D'), (2, '3D')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.ForeignKey(on_delete='CASCADE', related_name='sessao_filme', to='reserva.Filme')),
                ('sala', models.ForeignKey(on_delete='CASCADE', related_name='sessao_sala', to='reserva.Sala')),
            ],
        ),
        migrations.CreateModel(
            name='Poltrona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.CharField(max_length=2)),
                ('tipo', models.IntegerField(choices=[(1, 'Simples'), (2, 'Namoradeira'), (3, 'Cadeirante'), (4, 'Acompanhante')], default=1)),
                ('cliente', models.ForeignKey(on_delete='CASCADE', related_name='poltrona_cliente', to='reserva.Cliente')),
                ('sala', models.ForeignKey(on_delete='CASCADE', related_name='poltrona_sala', to='reserva.Sala')),
            ],
        ),
    ]
