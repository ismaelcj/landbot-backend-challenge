run:
	docker compose up --build -d

run-tests:
	docker compose exec app poetry run pytest --cov=src
