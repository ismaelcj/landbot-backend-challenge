from sqlalchemy.orm import Mapped, mapped_column

from src.backoffice.domain.team_notifier_config import TeamNotifierConfig
from src.shared.infrastructure.persistence.database import SQLBase


class TeamNotifierConfigRecord(SQLBase):
    __tablename__ = "team_notifier_config"

    topic: Mapped[str] = mapped_column(primary_key=True)
    method: Mapped[str] = mapped_column()
    destination: Mapped[str] = mapped_column()

    @classmethod
    def from_entity(cls, config: TeamNotifierConfig) -> "TeamNotifierConfigRecord":
        return cls.from_primitives(config.to_primitives())

    @classmethod
    def from_primitives(cls, data: dict) -> "TeamNotifierConfigRecord":
        return cls(
            topic=data["topic"],
            method=data["method"],
            destination=data["destination"],
        )

    def to_entity(self) -> TeamNotifierConfig:
        return TeamNotifierConfig.from_primitives(**self.to_primitives())

    def to_primitives(self) -> dict:
        return {
            "topic": self.topic,
            "method": self.method,
            "destination": self.destination
        }
