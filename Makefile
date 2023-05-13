run:
	python manage.py runserver

migrate:
	python manage.py migrate

migr:
	python manage.py makemigrations && make migrate