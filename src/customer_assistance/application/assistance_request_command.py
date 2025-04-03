from dataclasses import dataclass

from src.shared.domain.cqrs.command import Command


@dataclass(frozen=True)
class AssistanceRequestCommand(Command):
    assistance_id: str
    topic: str
    description: str
