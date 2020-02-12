## ABSTRACT

Ore impiegate nello sviluppo: circa 10. Ho deciso prima di iniziare che avrei speso 9 ore sul progetto, e poi avrei sistemato e documentato quanto prodotto compreso di BUG irrisolti e TODO list riportati in NOTE.md

L'applicativo è delineato nei suoi requisiti.

Gli utenti anonimi possono ricercare e visualizzare ricette

Gli utenti normali possono inserire ricette

L'utente amministratore crea utenti, ingredienti e eventualmente gestisce le ricette

In NOTE.md ci sono degli appunti sparsi presi durante lo svluppo per documentare un poco i ragionamenti, le problematiche e le soluzioni adottate.

L'applciativo è stato sviluppato e provato solo attraverso il web server di test, non è pronto per il deploy, anche perchè non era indicato alcun ambiente di deploy nelle specifiche. Mancano pagine generiche per gestire gli errori, il debug è attivo, non ho configurato alcun .gitignore per escludere file dal repo, ecc...


## CONFIGURAZIONE AMBIENTE DI SVILUPPO

Riporto in sintesi i passaggi effettuati per prepare l'ambiente di sviluppo. Maggiori info in NOTE.md

La versione di django pacchetizzata per kali (debian testing) che ho utilizzato come piattaforma per lo sviluppo è la 1.11.23. Dal sito di django apprendo che è la versione in LTS, ma il supporto terminerà a aprile 2020.  

Non installo quindi il pacchetto, ma scarico dal repo git di django la versione 3.1, così sono anche più allineato con la documentazione ufficciale di django.

`git clone https://github.com/django/django.git`

Creo un virtualenv all'interno del quale sviluppare

`mkvirtualenv django`

aggiorno pip e setuptools

`python3 -m pip install --upgrade pip setuptools`

installo django

`python3 -m pip install -e django/`

install il modulo django_country

`python3 -m pip install django-countries`


## INSTALLAZIONE ricettario

`git clone https://github.com/fg4mm/ricettario.git`

quindi eseguire se necessario la configurazione dell'ambiente di sviluppo (## CONFIGURAZIONE AMBIENTE DI SVILUPPO)


## TEST

`make server`

oppure

`python3 manage.py runserver`

e visitare

`http://127.0.0.1:8000`

Il db contiene gia' un utente superuser e due utenti normali

* admin@lan.net:admin
* user@lan.net:user
* user2@lan.net:user2

Nel db sono già presenti alcune ricette e ingredienti di test.
