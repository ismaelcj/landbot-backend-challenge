import datetime
from abc import ABC, abstractmethod
from typing import Optional

from src.shared.domain.value_object.custom_uuid import Uuid


class DomainEvent(ABC):
    def __init__(
            self,
            aggregate_id: str,
            event_id: Optional[str] = None,
            occurred_on: Optional[str] = None
    ) -> None:
        self.aggregate_id = aggregate_id
        self.event_id = event_id if event_id else Uuid.generate()
        self.occurred_on = occurred_on if occurred_on else \
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    @abstractmethod
    def event_name(self) -> str:
        pass

    @abstractmethod
    def to_primitives(self) -> dict:
        pass

    @classmethod
    def name(cls) -> str:
        return cls.__name__
