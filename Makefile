build:
	docker-compose build
up:
	docker-compose up --detach
down:
	docker-compose down
migrate:
	docker-compose run app python manage.py migrate
install-requirements:
	docker-compose run app pip install -r requirements.txt
populate-database:
	docker-compose run app python manage-database.py populate
backup-database:
	docker-compose run app python manage-database.py backup $(ARGS)
restore-database:
	docker-compose run app python manage-database.py restore $(ARGS)
