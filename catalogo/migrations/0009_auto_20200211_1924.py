# Generated by Django 3.1 on 2020-02-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_auto_20200211_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientiricette',
            name='ingrediente',
        ),
        migrations.AddField(
            model_name='ingredientiricette',
            name='ingrediente',
            field=models.ManyToManyField(null=True, to='catalogo.Ingrediente'),
        ),
        migrations.RemoveField(
            model_name='ingredientiricette',
            name='ricetta',
        ),
        migrations.AddField(
            model_name='ingredientiricette',
            name='ricetta',
            field=models.ManyToManyField(null=True, to='catalogo.Ricetta'),
        ),
    ]
