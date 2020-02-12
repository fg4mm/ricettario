# Generated by Django 3.1 on 2020-02-11 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0011_auto_20200211_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientiricette',
            name='ingrediente',
        ),
        migrations.AddField(
            model_name='ingredientiricette',
            name='ingrediente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Ingrediente'),
        ),
    ]
