dc = docker-compose

run:
	$(dc) up -d backend

setup-db:
	$(dc) up -d db
	$(dc) run --rm backend alembic upgrade head

alembic:
	$(dc) run --rm backend alembic revision --autogenerate -m $(msg)

build:
	docker build ./src -t platform_api

test:
	$(dc) run -e POSTGRES_DB="platform_api_testdb" backend pytest

build-test: build test