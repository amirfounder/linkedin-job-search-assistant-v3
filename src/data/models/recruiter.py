from typing import Optional, Dict

from commons.daos.json_index import JsonIndexModel as Model
from pydantic import Field


class TouchPoint(Model):
    value: Optional[bool] = Field(default=False)


class Profile(Model):
    name: str
    company: Optional[str]
    headline: str
    first_name: str
    linkedin_url: str
    username: Optional[str]


class Recruiter(Model):
    username: str
    profile: Profile
    touchpoints: Optional[Dict[str, Optional[TouchPoint]]]
