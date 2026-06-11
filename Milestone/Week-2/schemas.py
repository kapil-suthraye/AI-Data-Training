from pydantic import BaseModel, Field
from typing import Literal


class SummariseRequest(BaseModel):
    text: str = Field(min_length=20)
    style: Literal["brief", "detailed"]


class SummariseResponse(BaseModel):
    summary: str
    model: str
    input_chars: int