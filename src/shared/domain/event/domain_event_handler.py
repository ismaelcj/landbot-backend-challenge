from abc import ABC, abstractmethod

from src.shared.domain.event.domain_event import DomainEvent


class DomainEventHandler(ABC):

    def __call__(self, *args, **kwargs):
        return self.handle(*args, **kwargs)

    @abstractmethod
    def handle(self, event: DomainEvent) -> None:
        pass
