from abc import ABC, abstractmethod
from typing import List, Type

from src.shared.domain.event.domain_event import DomainEvent
from src.shared.domain.event.domain_event_handler import DomainEventHandler


class EventBus(ABC):

    @abstractmethod
    def subscribe(self, event_type: Type[DomainEvent], handler: DomainEventHandler) -> None:
        pass

    @abstractmethod
    def publish(self, events: List[DomainEvent]) -> None:
        pass
