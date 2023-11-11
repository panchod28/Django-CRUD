# Generated by Django 4.1.13 on 2023-11-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculos',
            name='VehiculoNombre',
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='ano',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='estado',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='identificador',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='imagen',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='marca',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='modelo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='tipo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='valorDia',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
