from typing import Annotated
from sqlalchemy.orm import Session

from fastapi import Depends

from src.backoffice.application.event_handlers.notify_team_on_assistance_created import NotifyTeamOnAssistanceCreated
from src.backoffice.application.commands.team_notifier_config_create_command import TeamNotifierConfigCreateCommand
from src.backoffice.application.commands.team_notifier_config_create_command_handler import \
    TeamNotifierConfigCreateCommandHandler
from src.backoffice.infrastructure.persistance.sqlalchemy_team_notifier_config_repository import \
    SqlalchemyTeamNotifierConfigRepository
from src.customer_assistance.application.assistance_request_command import AssistanceRequestCommand
from src.customer_assistance.application.assistance_request_command_handler import AssistanceRequestCommandHandler
from src.customer_assistance.domain.assistance_created_event import AssistanceCreatedEvent
from src.customer_assistance.infrastructure.sqlalchemy_asistance_repository import SqlalchemyAssistanceRepository
from src.shared.infrastructure.cqrs.memory_command_bus import MemoryCommandBus
from src.shared.infrastructure.event.memory_event_bus import MemoryEventBus
from src.shared.infrastructure.persistence.database import get_db


event_bus = MemoryEventBus()
command_bus = MemoryCommandBus()

def initial_setup(db: Session = next(get_db())) -> None:
    assistance_repository = SqlalchemyAssistanceRepository(db_session=db)
    assistance_request_handler = AssistanceRequestCommandHandler(
        assistance_repository=assistance_repository,
        event_bus=event_bus,
    )
    command_bus.register(AssistanceRequestCommand, assistance_request_handler)

    team_notifier_config_repo = SqlalchemyTeamNotifierConfigRepository(db_session=db)
    team_notifier_create_handler = TeamNotifierConfigCreateCommandHandler(
        config_repository=team_notifier_config_repo,
        event_bus=event_bus
    )
    command_bus.register(TeamNotifierConfigCreateCommand, team_notifier_create_handler)

    notify_team_on_assistance_created = NotifyTeamOnAssistanceCreated(team_notifier_config_repo)
    event_bus.subscribe(AssistanceCreatedEvent, notify_team_on_assistance_created)


def get_command_bus():
    return command_bus

CommandBus = Annotated[MemoryCommandBus, Depends(get_command_bus)]
