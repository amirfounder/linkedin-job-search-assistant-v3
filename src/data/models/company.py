from datetime import datetime
from typing import Optional

from commons.daos import JsonIndexModel, JsonIndexSubModel
from commons.helpers import now
from pydantic import Field


class Interaction(JsonIndexSubModel):
    timestamp: datetime = Field(default_factory=now)
    recruiter_username: Optional[str]
    touchpoints_updated: Optional[list] = Field(default_factory=list)


class Company(JsonIndexModel):
    name: Optional[str]
    last_interaction: Optional[Interaction]
    interactions: Optional[list[Interaction]] = Field(default_factory=list)
