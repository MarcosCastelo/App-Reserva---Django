# Generated by Django 2.2 on 2019-07-31 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poltrona',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete='CASCADE', related_name='poltrona_cliente', to='reserva.Cliente'),
        ),
    ]
