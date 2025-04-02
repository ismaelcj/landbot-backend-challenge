from sqlalchemy.orm import Mapped, mapped_column

from src.customer_assistance.domain.assistance import Assistance
from src.shared.infrastructure.persistence.database import SQLBase


class AssistanceRecord(SQLBase):
    __tablename__ = "customer_assistance"

    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=False)
    topic: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    @classmethod
    def from_entity(cls, assistance: Assistance) -> "AssistanceRecord":
        return cls.from_primitives(assistance.to_primitives())

    @classmethod
    def from_primitives(cls, data: dict) -> "AssistanceRecord":
        return cls(
            id=data["id"],
            topic=data["topic"],
            description=data["description"],
        )

    def to_entity(self) -> Assistance:
        return Assistance.from_primitives(**self.to_primitives())

    def to_primitives(self) -> dict:
        return {
            "id": self.id,
            "topic": self.topic,
            "description": self.description,
        }
