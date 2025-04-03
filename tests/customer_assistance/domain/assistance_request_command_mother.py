import uuid

from src.customer_assistance.application.assistance_request_command import AssistanceRequestCommand
from src.customer_assistance.domain.assistance_topic import AssistanceTopic


class AssistanceRequestCommandMother:
    @staticmethod
    def create(assistance_id: str = uuid.uuid4().hex,
               topic: str = AssistanceTopic.SALES.value,
               description: str = "test-description") -> AssistanceRequestCommand:
        return AssistanceRequestCommand(
            assistance_id=assistance_id,
            topic=topic,
            description=description
        )
