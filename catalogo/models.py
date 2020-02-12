from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# Create your models here.

#Estendo il modello User con i campi gender e birthday_date. 
#Uso la mail in luogo dello username per il login.
class User(AbstractUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(
		unique=True,
		blank=True
    )
    MASCHIO = 'Maschio'
    FEMMINA = 'Femmina'
    NONDICHIARATO = 'Non dichiarato'
    gender_choices = [
            (MASCHIO, 'Maschio'),
            (FEMMINA, 'Femmina'),
            (NONDICHIARATO, 'Non dichiarato')
    ]
    gender = models.CharField(
        max_length=15,
        choices=gender_choices,
        verbose_name="Genere",
        default=NONDICHIARATO
    )
    birth_date = models.DateField(
        verbose_name="Data di nascita",
        null=True, 
        blank=True
    )


#Per il campo nazionalita utilizzo l'app django-countries
class Ricetta(models.Model):
    nome = models.CharField(
        max_length=200,
        null=False,
        default="Ricetta"
    )
    ANTIPASTO = 'Antipasto'
    PRIMO = 'Primo'
    SECONDO = 'Secondo'
    CONTORNO = 'Contorno'
    DOLCE = 'Dolce'
    tipo_choices = [
        (ANTIPASTO,'Antipasto'),
        (PRIMO,'Primo'),
        (SECONDO,'Secondo'),
        (CONTORNO,'Contorno'),
        (DOLCE,'Dolce')
    ]
    tipo = models.CharField(
        max_length=15,
        choices=tipo_choices,
        default=ANTIPASTO
    )
    autore = models.ForeignKey(
            User, 
            on_delete=models.SET_NULL, 
            null=True
    )
    FACILE = 'Facile'
    MEDIA = 'Media'
    DIFFICILE = 'Difficile'
    difficolta_choices = [
        (FACILE, 'Facile'),
        (MEDIA, 'Media'),
        (DIFFICILE, 'Difficile')
    ]
    difficolta = models.CharField(
        verbose_name = 'Difficoltà',
        max_length=15,
        choices=difficolta_choices,
        default=FACILE
    )
    immagine = models.ImageField(
        upload_to ='ricette',
        default = 'default.jpg'
    )
    descrizione = models.TextField(
        max_length=4000,
        null=True,
    )
    nazionalita = CountryField(
        verbose_name = 'Nazionalità',
    )

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name = 'Nome',
        null=False,
        default="Ingrediente"
    )
    calorie = models.IntegerField(
        verbose_name = 'Calorie',
        default="0"
    )

    def __str__(self):
        return self.nome

class IngredientiRicette(models.Model):
    ingrediente = models.ForeignKey(
            Ingrediente,
            on_delete=models.CASCADE,
            null=True
    )
    ricetta = models.ForeignKey(
            Ricetta, 
            on_delete=models.CASCADE,
            null=True
    )
    quantita = models.CharField(
        max_length=200,
        verbose_name="Quantità" 
    )

    class Meta:
        unique_together = (("ingrediente", "ricetta"),)

    def __str__(self):
        return "%s" % self.ingrediente
