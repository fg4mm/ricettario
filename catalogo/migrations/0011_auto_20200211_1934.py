# Generated by Django 3.1 on 2020-02-11 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_auto_20200211_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientiricette',
            name='ricetta',
        ),
        migrations.AddField(
            model_name='ingredientiricette',
            name='ricetta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Ricetta'),
        ),
    ]
