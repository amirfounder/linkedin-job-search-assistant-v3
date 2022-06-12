from typing import Optional, Dict

from commons.daos.json_index import JsonIndexModel as Model


class TouchPoint(Model):
    is_complete: Optional[int]


class Recruiter(Model):
    name: str
    username: str
    company: Optional[str]
    headline: Optional[str]
    touchpoints: Dict[str, Optional[TouchPoint]]
