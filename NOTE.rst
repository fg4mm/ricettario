===================================
CONFIGURAZIONE AMBIENTE DI SVILUPPO
===================================

La versione di django pacchetizzata per kali (debian testing) è la 1.11.23. Dal sito di django apprendo che è la versione in LTS, ma il supporto terminerà a aprile 2020.  

Non installo quindi il pacchetto, ma scarico dal repo git di django la versione 3.1, così sono più allineato con la documentazione ufficciale di django.

Creo un virtualenv all'interno del quale sviluppare

mkvirtualenv django

aggiorno pip e setuptools

python3 -m pip install --upgrade pip setuptools

installo django

python3 -m pip install -e django/

Creo un progetto ricette

django-admin startproject ricette


================
NOTE DI SVILUPPO
================

===============
Modellizzazione
===============

Gli utenti sono definiti da alcuni campi non presenti nello schema di django, altri invece coincidono.  Posso quindi estendere la classe AbstractUser per aggiungere i due campi mancanti.

L'applicativo si presenta come un ricettario, un catalogo di ricette.

Una ricetta ha un autore che coincide con l'utente loggato, autore avrà quindi una ForeignKey su User (controllare come gestire le varie AbstractView per passare il campo autore dall'oggetto user e toglierlo dal form)

Le ricette sono composte da ingrendienti, serve quindi una tabella a parte per gli ingredienti, che sono inseriti solo dall'amministratore. Esiste quindi azioni accessibili solo all'amministratore, all'utente autenticato e non.

Amministratore: 
elenca,visualizza,crea,cancella,aggiorna utenti
elenca,visualizza,crea,cancella,aggiorna ricette
elenca,visualizza,crea,cancella,aggiorna ingredienti

Utente autenticato:
elenca,visualizza,crea,cancella,aggiorna le proprie ricette

Utente non autenticato:
elenca,visualizza le ricette

L'aggiunta di ingredienti a una ricetta, implica l'esistenza di una tabella che associ
un ingrediente a una ricetta.

L'applicativo consterà quindi di 4 modelli:

User che estende AbstractUer
Ricetta legata a User dall'autore
Ingrediente con l'elenco degli ingredienti inserito da admin
IngredienteToRicetta che collega un Ingridiente a una Ricetta, questo modello contiene anche il campo quantità, che sarà un campo di testo libero, perchè le unità di misura usate in cucina sono le più svariate (gr,etti,chili,litri,pizzichi,pugnetti,tazze,tazzine,cucchiai)

================
Views e template
================

====
User
====

La gestione degli utenti è deputata al solo superuser. utilizzo userpassestest come decoratore e come classe per controllare se user is_superuser

ho definito 4 view

manageUser: presenta un elenco di utenti e ne permette la gestione, attualmente admin può rimuovere sè stesso, che non va troppo bene
createUser: crea un utente con i campi strettamente necessari, la passsword viene presa dall'utente e convertita nel formato di default di django con make_password()
deleteUser: 
updateUser: 

Il campo password andrebbe forzato a essere Inpufield di tipo password, per ora e' un campo di testo semplice

Non riesco a far funzionare il campo immagine con ImageField, ho settato MEDIA_URL e MEDIA_PATH e modoficato la sezione TEMPLATES in settings.py, ma le immagini non vengono caricate nella cartella. Rimane come BUG.

=======
Ricetta
=======

index: nel caso di utente anonimo presenta le ultime 5 ricette pubblicate, altrimenti l'elenco di tutte le ricette per admin e solodelle proprie per user
search: ricerca nei campi nome e descrizione della ricetta https://docs.djangoproject.com/en/3.0/topics/db/queries/#complex-lookups-with-q-objects
showRicetta: mostra una ricetta ricercando anche gli ingredienti relativi in IngredientiRicette
manageRicetta
createRicetta
updateRicetta
deleteRicetta

Le operazioni sulle ricette sono consentite solo al superuser o all'autore della ricetta

===========
Ingrediente
===========

Il superuser aggiunge gli ingredienti che gli utenti possono utilizzare per le ricette

manageIngrediente
createIngrediente
deleteIngrediente
updateIngrediente

==================
IngredientiRicette
==================

Un utente può aggiungere ingredienti a una ricetta creata da lui.

createIngredientiToRicetta:
deleteIngredientiToRicetta: sviluppata ma non inserita nell'interfaccia

In generale non ho avuto tempo di creare un modo comodo per aggiungere un ingrediente a una ricetta,
andrebbe preparato qualcosa con ajax per aggiungere un ingrediente direttamente nella pagina di visualizzazione
della ricetta, ma non ho tempo di farlo

