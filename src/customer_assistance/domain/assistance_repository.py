from abc import ABC, abstractmethod

from src.customer_assistance.domain.assistance import Assistance


class AssistanceRepository(ABC):
    @abstractmethod
    def save(self, assistance: Assistance) -> None:
        pass

    @abstractmethod
    def find_by_id(self, assistance_id: str) -> Assistance:
        pass
