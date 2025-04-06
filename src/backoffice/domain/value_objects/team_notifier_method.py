from enum import Enum


class TeamNotifierMethod(Enum):

    EMAIL = "email"
    SLACK = "slack"

    def __str__(self) -> str:
        return self.value
