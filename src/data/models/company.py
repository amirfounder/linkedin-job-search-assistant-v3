from datetime import datetime
from typing import Optional

from commons.daos import JsonIndexModel, JsonIndexSubModel
from commons.helpers import now
from pydantic import Field


class Interaction(JsonIndexSubModel):
    timestamp: datetime = Field(default_factory=now)
    recruiter_username: Optional[str] = Field(default=None)
    touchpoints_updated: Optional[list] = Field(default_factory=list)


class Company(JsonIndexModel):
    name: Optional[str] = Field(default=None)
    last_interaction: Optional[Interaction] = Field(default=None)
    interactions: Optional[list[Interaction]] = Field(default_factory=list)
    aliases: Optional[list[str]] = Field(default_factory=list)


class CompanyAlias(JsonIndexModel):
    alias_for: Optional[str] = Field(default=None)
