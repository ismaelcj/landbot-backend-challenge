from src.shared.domain.event.domain_event import DomainEvent


class AssistanceCreatedEvent(DomainEvent):

    def __init__(self, assistance_id: str, topic: str, description: str) -> None:
        super().__init__(assistance_id)
        self.topic = topic
        self.description = description

    @property
    def event_name(self) -> str:
        return "landbot.customer_assistance.assistance.created"

    def to_primitives(self) -> dict:
        return {
            'id': self.aggregate_id,
            'topic': self.topic,
            'description': self.description
        }
