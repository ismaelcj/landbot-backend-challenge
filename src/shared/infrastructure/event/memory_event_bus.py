from collections import defaultdict
from typing import List, Type

from src.shared.domain.event.domain_event import DomainEvent
from src.shared.domain.event.domain_event_handler import DomainEventHandler
from src.shared.domain.event.event_bus import EventBus


class MemoryEventBus(EventBus):

    def __init__(self) -> None:
        self._subscriptions: dict = defaultdict(list)

    def subscribe(self, event_type: Type[DomainEvent], handler: DomainEventHandler) -> None:
        self._subscriptions[event_type].append(handler)

    def publish(self, events: List[DomainEvent]) -> None:
        for event in events:
            event_classes = [cls for cls in event.__class__.__mro__ if cls != object]

            handlers = []
            for event_class in event_classes:
                handlers.extend(self._subscriptions.get(event_class, []))

            for handler in handlers:
                handler(event)
