import uuid
from pprint import pprint

from src.shared.domain.value_object.value_object import ValueObject


class Uuid(ValueObject):
    def __init__(self, value: str) -> None:
        self.ensure_valid_uuid(value)
        super().__init__(value)

    @staticmethod
    def ensure_valid_uuid(value: str) -> None:
        pprint(f"ensure_valid_uuid: {value}")
        try:
            uuid.UUID(value)
        except ValueError:
            raise ValueError(f"Invalid UUID: {value}")

    @staticmethod
    def generate() -> str:
        return str(uuid.uuid4())
