from dataclasses import dataclass

from src.shared.domain.cqrs.command import Command


@dataclass(frozen=True)
class TeamNotifierConfigCreateCommand(Command):
    topic: str
    method: str
    destination: str
