from pydantic import BaseModel


class Input(BaseModel):
    mail_body: str


class PredictedEntity(BaseModel):
    entity_text: str
    start: int
    end: int
