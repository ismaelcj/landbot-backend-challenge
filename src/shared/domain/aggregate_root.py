from abc import ABC

from src.shared.domain.event.domain_event import DomainEvent


class AggregateRoot(ABC):
    def __init__(self) -> None:
        self._domain_events = list[DomainEvent]()

    def record_event(self, event: DomainEvent) -> None:
        self._domain_events.append(event)

    def pull_domain_events(self) -> list[DomainEvent]:
        domain_events = self._domain_events
        self._domain_events = []
        return domain_events
