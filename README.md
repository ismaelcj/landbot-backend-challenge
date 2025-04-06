# Landbot Backend Challenge

### Principles and arquitecture
This project has been built based on the Hexagonal architecture + DDD + CQRS principles.

For this purpose, the following main technologies that have been chosen are:
- FastAPI, as API Framework
- SQLAlchemy, as ORM
- Uvicorn, as ASGI web server

### EventBus and CQRS
For event and command management, an EventBus and a CommandBus have been created in a simple memory style.
The QueryBus has been skipped as is not used.

### Bounded contexts
Two bounded contexts, `customer_assistance` and `backoffice`, have been forced in order to emphasise the separation of domains.

### Team Notifier Config
[TeamNotifierConfig](/src/backoffice/domain/team_notifier_config.py) is a simulation of a backoffice configuration where the team can choose some application behaviours.

For example, doing a call like the following. You are able to configure the application to notify the finance team every time a pricing question is raised by a customer.
```bash
curl -X PUT http://localhost:8000/backoffice/team_notifier_config \
  -H "Content-Type: application/json" \
  -d '{"topic": "assistance.pricing", "method": "slack", "destination": "#finance-team"}'
```

Then an assistance request can be created with the following request.
And the application will notify the finance team using the Slack channel configured in the previous step.
```bash
curl -X POST http://localhost:8000/assistance_request \
  -H "Content-Type: application/json" \
  -d '{"assistance_id": "123e4567-e89b-12d3-a456-426614174000", "topic": "pricing", "description": "I have a problem with my last invoice"}'
```




---

## Build and run the project
```bash
make build
```

## Run tests and see coverage
```bash
make run-tests
```

## OpenAPI Docs
[http://localhost:8000/docs](http://localhost:8000/docs)
