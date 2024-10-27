# Project settings
DJANGO_MANAGE = uv run manage.py
DJANGO_APP_NAME = books


.PHONY: help run migrate makemigrations shell test collectstatic

help:
	@echo "Django Makefile"
	@echo "Available commands:"
	@echo "  make run-dev           - Run the development server"
	@echo "  make run-watch         - Run the development server inside a docker container"
	@echo "  make run-prod          - Run the production server"
	@echo "  make stop         		- Stop the docker "
	@echo "  make migrate        - Apply database migrations locally for SQLite"
	@echo "  make makemigrations - Create new migrations based on changes"
	@echo "  make shell          - Open the Django shell"
	@echo "  make test           - Run tests"
	@echo "  make collectstatic  - Collect static files"

run-dev:
	$(DJANGO_MANAGE) runserver

run-watch:
	docker compose watch

run-prod:
	docker compose up --build -d

stop:
	docker compose stop

migrate:
	$(DJANGO_MANAGE) migrate

makemigrations:
	$(DJANGO_MANAGE) makemigrations $(DJANGO_APP_NAME)

shell:
	$(DJANGO_MANAGE) shell

test:
	$(DJANGO_MANAGE) test

test-postgres:
	docker compose up backend-test

collectstatic:
	$(DJANGO_MANAGE) collectstatic

