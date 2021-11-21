run.site:
	poetry run ./manage.py runserver

build.site:
	time poetry run ./manage.py build -v 3 --settings settings.production
