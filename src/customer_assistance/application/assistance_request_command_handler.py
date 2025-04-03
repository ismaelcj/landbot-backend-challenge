from src.customer_assistance.application.assistance_request_command import AssistanceRequestCommand
from src.customer_assistance.domain.assistance import Assistance
from src.customer_assistance.domain.assistance_repository import AssistanceRepository
from src.shared.domain.cqrs.command_handler import CommandHandler
from src.shared.domain.event.event_bus import EventBus


class AssistanceRequestCommandHandler(CommandHandler):
    def __init__(self, assistance_repository: AssistanceRepository, event_bus: EventBus) -> None:
        self.__assistance_repository = assistance_repository
        self.__event_bus = event_bus

    def handle(self, command: AssistanceRequestCommand) -> None:
        assistance = Assistance.create(
            command.assistance_id,
            command.topic,
            command.description
        )
        self.__assistance_repository.save(assistance)
        self.__event_bus.publish(assistance.pull_domain_events())
