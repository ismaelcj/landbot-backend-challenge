from pydantic import BaseModel


class AssistanceRequest(BaseModel):
    assistance_id: str
    topic: str
    description: str
