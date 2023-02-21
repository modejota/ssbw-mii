build:
	docker-compose build
up:
	docker-compose up --detach
down:
	docker-compose down
migrate:
	docker-compose run app python manage.py migrate
makemigrations:
	docker-compose run app python manage.py makemigrations ssbwproject
populate-database:
	docker-compose run app python populate-database.py
drop-database:
	sudo rm -rf datos_db