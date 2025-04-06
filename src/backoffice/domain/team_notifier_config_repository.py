from abc import ABC, abstractmethod

from src.backoffice.domain.team_notifier_config import TeamNotifierConfig


class TeamNotifierConfigRepository(ABC):
    @abstractmethod
    def save(self, config: TeamNotifierConfig) -> None:
        pass

    @abstractmethod
    def find_by_topic(self, topic: str) -> TeamNotifierConfig:
        pass

    @abstractmethod
    def exists(self, topic: str) -> bool:
        pass