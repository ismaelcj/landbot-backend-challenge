from enum import Enum


class AssistanceTopic(Enum):

    SALES = "sales"
    PRICING = "pricing"

    def __str__(self) -> str:
        return self.value
