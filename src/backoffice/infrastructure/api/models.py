from pydantic import BaseModel


class TeamNotifierConfigModel(BaseModel):
    topic: str
    method: str
    destination: str
