build:
	docker compose up --build -d
	docker compose exec app alembic init migrations

re-build:
	docker compose down
	docker compose up --build -d

run:
	docker compose up -d

run-tests:
	docker compose exec app poetry run pytest --cov=src

makemigrations:
	docker compose exec app alembic revision --autogenerate -m "$(message)"

migrate:
	docker compose exec app alembic upgrade head
