import uuid

from src.customer_assistance.domain.assistance import Assistance
from src.customer_assistance.domain.assistance_topic import AssistanceTopic


class AssistanceMother:
    @staticmethod
    def create(assistance_id: str = uuid.uuid4().hex,
               topic: str = AssistanceTopic.SALES.value,
               description: str = "test-description") -> Assistance:
        return Assistance.create(
            assistance_id=assistance_id,
            topic=topic,
            description=description
        )
