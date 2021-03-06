# Generated by Django 3.1 on 2020-02-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20200210_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ricetta',
            name='difficolta',
            field=models.CharField(choices=[('Facile', 'Facile'), ('Media', 'Media'), ('Difficile', 'Difficile')], default='Facile', max_length=15, verbose_name='Difficoltà'),
        ),
        migrations.AlterField(
            model_name='ricetta',
            name='tipo',
            field=models.CharField(choices=[('Antipasto', 'Antipasto'), ('Primo', 'Primo'), ('Secondo', 'Secondo'), ('Contorno', 'Contorno'), ('Dolce', 'Dolce')], default='Antipasto', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Maschio', 'Maschio'), ('Femmina', 'Femmina'), ('Non dichiarato', 'Non dichiarato')], default='N', help_text='Genere', max_length=15),
        ),
    ]
