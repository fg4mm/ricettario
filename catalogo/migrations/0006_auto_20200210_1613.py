# Generated by Django 3.1 on 2020-02-10 15:13

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_ricetta_autore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ricetta',
            name='descrizione',
            field=models.TextField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='ricetta',
            name='difficolta',
            field=models.CharField(choices=[('F', 'Facile'), ('M', 'Media'), ('D', 'Difficile')], default='F', max_length=1, verbose_name='Difficoltà'),
        ),
        migrations.AlterField(
            model_name='ricetta',
            name='nazionalita',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='Nazionalità'),
        ),
        migrations.AlterField(
            model_name='ricetta',
            name='nome',
            field=models.CharField(default='Ricetta', max_length=200),
        ),
        migrations.AlterField(
            model_name='ricetta',
            name='tipo',
            field=models.CharField(choices=[('A', 'Antipasto'), ('P', 'Primo'), ('S', 'Secondo'), ('C', 'Contorno'), ('D', 'Dolce')], default='A', max_length=1),
        ),
    ]
