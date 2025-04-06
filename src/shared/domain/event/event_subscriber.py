from abc import ABC, abstractmethod
from typing import Callable, Any


class EventSubscriber(ABC):
    """Interface for event subscribers."""
    
    @abstractmethod
    def subscribe(self, callback: Callable[[dict], Any]) -> None:
        """
        Subscribe to events and process them with the provided callback.
        
        Args:
            callback: Function that processes the event data.
                     It receives the event data as a dictionary and can return any value.
        """
        pass
