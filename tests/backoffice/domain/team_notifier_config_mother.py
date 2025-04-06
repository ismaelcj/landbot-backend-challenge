from src.backoffice.domain.team_notifier_config import TeamNotifierConfig
from src.backoffice.domain.value_objects.team_notifier_method import TeamNotifierMethod
from src.backoffice.domain.value_objects.team_notifier_topic import TeamNotifierTopic


class TeamNotifierConfigMother:
    @staticmethod
    def create(topic: str = TeamNotifierTopic.SALES_ASSISTANCE.value,
               method: str = TeamNotifierMethod.SLACK.value,
               destination: str = "#channel-test"
    ):  
        return TeamNotifierConfig.create(
            topic=topic,
            method=method,
            destination=destination,
        )
