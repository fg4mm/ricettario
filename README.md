===================================
CONFIGURAZIONE AMBIENTE DI SVILUPPO
===================================

La versione di django pacchetizzata per kali (debian testing) che ho utilizzato come piattaforma per lo sviluppo è la 1.11.23. Dal sito di django apprendo che è la versione in LTS, ma il supporto terminerà a aprile 2020.  

Non installo quindi il pacchetto, ma scarico dal repo git di django la versione 3.1, così sono anche più allineato con la documentazione ufficciale di django.

git clone https://github.com/django/django.git

Creo un virtualenv all'interno del quale sviluppare

mkvirtualenv django

aggiorno pip e setuptools

python3 -m pip install --upgrade pip setuptools

installo django

python3 -m pip install -e django/

Creo un progetto ricette

django-admin startproject ricette


