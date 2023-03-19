setup:
	cp .env.example .env

migrate:
	docker-compose exec web ./manage.py migrate

makemigrations:
	docker-compose exec web ./manage.py makemigrations

shell:
	docker-compose exec web ./manage.py shell

createsuperuser:
	docker-compose exec web ./manage.py createsuperuser

test:
	docker-compose exec web pytest tests/ -s
