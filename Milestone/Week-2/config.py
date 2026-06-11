import yaml

from pydantic import BaseModel
from typing import Literal


class LLMConfig(BaseModel):
    provider: Literal["groq"]
    model: str
    max_tokens: int


class AppConfig(BaseModel):
    service_name: str
    port: int
    log_level: str
    llm: LLMConfig


def load_config(path: str):
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    return AppConfig.model_validate(data)