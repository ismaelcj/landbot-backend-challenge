from src.backoffice.application.notifiers.team_notifier_factory import TeamNotifierFactory
from src.backoffice.domain.team_notifier_config_repository import TeamNotifierConfigRepository
from src.customer_assistance.domain.assistance_created_event import AssistanceCreatedEvent
from src.shared.domain.event.domain_event_handler import DomainEventHandler


class NotifyTeamOnAssistanceCreated(DomainEventHandler):
    def __init__(self, config_repository: TeamNotifierConfigRepository):
        self.__config_repository = config_repository

    def handle(self, event: AssistanceCreatedEvent) -> None:
        config = self.__config_repository.find_by_topic(f"assistance.{event.topic}")
        notifier = TeamNotifierFactory().get_notifier(config.method.value)()
        notifier.notify()
