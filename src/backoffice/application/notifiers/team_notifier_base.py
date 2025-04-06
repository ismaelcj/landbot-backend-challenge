from abc import ABC, abstractmethod


class TeamNotifierBase(ABC):

    @abstractmethod
    def notify(self):
        pass
