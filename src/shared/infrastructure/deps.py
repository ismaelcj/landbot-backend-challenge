from typing import Annotated
from sqlalchemy.orm import Session

from fastapi import Depends

from src.customer_assistance.application.assistance_request_command import AssistanceRequestCommand
from src.customer_assistance.application.assistance_request_command_handler import AssistanceRequestCommandHandler
from src.customer_assistance.domain.assistance_created_event import AssistanceCreatedEvent
from src.customer_assistance.infrastructure.sqlalchemy_asistance_repository import SqlalchemyAssistanceRepository
from src.shared.infrastructure.cqrs.memory_command_bus import MemoryCommandBus
from src.shared.infrastructure.event.memory_event_bus import MemoryEventBus
from src.shared.infrastructure.persistence.database import get_db


def setup_command_bus(db: Session = Depends(get_db)) -> MemoryCommandBus:
    command_bus = MemoryCommandBus()
    event_bus = MemoryEventBus()
    assistance_repository = SqlalchemyAssistanceRepository(db_session=db)

    assistance_request_handler = AssistanceRequestCommandHandler(
        assistance_repository=assistance_repository,
        event_bus=event_bus,
    )
    command_bus.register(AssistanceRequestCommand, assistance_request_handler)
    event_bus.subscribe(AssistanceCreatedEvent,

    return command_bus

CommandBus = Annotated[MemoryCommandBus, Depends(setup_command_bus)]
