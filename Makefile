dc = docker-compose

run:
	$(dc) up -d api

proxy:
	$(dc) up -d nginx

setup-db:
	$(dc) up -d db
	$(dc) run --rm api alembic upgrade head

alembic:
	$(dc) run --rm api alembic revision --autogenerate -m $(msg)

build:
	docker build ./src -t platform_api

test:
	$(dc) run --rm -e POSTGRES_DB="platform_api_testdb" api pytest

mock:
	$(dc) run --rm api python -m platform_api.mock

build-test: build test