from src.customer_assistance.domain.assistance_created_event import \
    AssistanceCreatedEvent
from src.customer_assistance.domain.assistance_topic import AssistanceTopic
from src.shared.domain.aggregate_root import AggregateRoot
from src.shared.domain.value_object.custom_uuid import Uuid


class Assistance(AggregateRoot):

    def __init__(
            self,
            assistance_id: Uuid,
            topic: AssistanceTopic,
            description: str
    ) -> None:
        super().__init__()
        self._id = assistance_id
        self._topic = topic
        self._description = description

    @classmethod
    def create(
            cls,
            assistance_id: str,
            topic: str,
            description: str
    ) -> "Assistance":
        assistance = cls(
            assistance_id=Uuid(assistance_id),
            topic=AssistanceTopic(topic),
            description=description
        )
        assistance.record_event(AssistanceCreatedEvent(
            assistance_id,
            topic,
            description
        ))
        return assistance

    @classmethod
    def from_primitives(
            cls,
            assistance_id: str,
            topic: str,
            description: str
    ) -> "Assistance":
        return cls(
            assistance_id=Uuid(assistance_id),
            topic=AssistanceTopic(topic),
            description=description
        )

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "topic": self._topic.value,
            "description": self._description
        }
