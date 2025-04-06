from src.backoffice.domain.value_objects.team_notifier_topic import TeamNotifierTopic
from src.backoffice.domain.value_objects.team_notifier_method import TeamNotifierMethod
from src.shared.domain.aggregate_root import AggregateRoot


class TeamNotifierConfig(AggregateRoot):

    def __init__(
            self,
            topic: TeamNotifierTopic,
            method: TeamNotifierMethod,
            destination: str
    ):
        super().__init__()
        self._topic = topic
        self._method = method
        self._destination = destination

    @classmethod
    def create(
            cls,
            topic: str,
            method: str,
            destination: str
    ):
        config = cls(
            topic=TeamNotifierTopic(topic),
            method=TeamNotifierMethod(method),
            destination=destination
        )
        return config

    @classmethod
    def from_primitives(
            cls,
            topic: str,
            method: str,
            destination: str
    ) -> "TeamNotifierConfig":
        return cls(
            topic=TeamNotifierTopic(topic),
            method=TeamNotifierMethod(method),
            destination=destination
        )

    def to_primitives(self) -> dict:
        return {
            "topic": self._topic.value,
            "method": self._method.value,
            "destination": self._destination
        }

    @property
    def method(self):
        return self._method
