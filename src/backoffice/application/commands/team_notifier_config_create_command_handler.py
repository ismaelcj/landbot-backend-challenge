from src.backoffice.application.commands.team_notifier_config_create_command import TeamNotifierConfigCreateCommand
from src.backoffice.domain.team_notifier_config import TeamNotifierConfig
from src.backoffice.domain.team_notifier_config_repository import TeamNotifierConfigRepository
from src.shared.domain.cqrs.command_handler import CommandHandler
from src.shared.domain.event.event_bus import EventBus


class TeamNotifierConfigCreateCommandHandler(CommandHandler):
    def __init__(self, config_repository: TeamNotifierConfigRepository, event_bus: EventBus) -> None:
        self.__config_repository = config_repository
        self.__event_bus = event_bus

    def handle(self, command: TeamNotifierConfigCreateCommand) -> None:
        self.ensure_config_not_exists(command.topic)
        config = TeamNotifierConfig.create(
            command.topic,
            command.method,
            command.destination
        )
        self.__config_repository.save(config)
        self.__event_bus.publish(config.pull_domain_events())

    def ensure_config_not_exists(self, topic):
        config_exists = self.__config_repository.exists(topic)
        if config_exists:
            raise ValueError(f"TeamNotifierConfig with topic '{topic}' already exists")
