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
            assistance_id: Uuid,
            topic: AssistanceTopic,
            description: str
    ) -> "Assistance":
        assistance = cls(assistance_id, topic, description)
        assistance.record_event(AssistanceCreatedEvent(
            assistance_id.value,
            topic.value,
            description
        ))
        return assistance
