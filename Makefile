PYTHON=/usr/bin/python3

migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate
	
server:
	$(PYTHON) manage.py runserver

shell:
	$(PYTHON) manage.py shell

