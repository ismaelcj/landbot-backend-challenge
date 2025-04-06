from src.backoffice.application.commands.team_notifier_config_create_command import TeamNotifierConfigCreateCommand
from src.backoffice.domain.value_objects.team_notifier_topic import TeamNotifierTopic
from src.backoffice.domain.value_objects.team_notifier_method import TeamNotifierMethod


class TeamNotifierConfigCreateCommandMother:
    @staticmethod
    def create(topic: str = TeamNotifierTopic.SALES_ASSISTANCE.value,
               method: str = TeamNotifierMethod.SLACK.value,
               destination: str = "#channel-test"
    ) -> TeamNotifierConfigCreateCommand:
        return TeamNotifierConfigCreateCommand(
            topic=topic,
            method=method,
            destination=destination
        )
