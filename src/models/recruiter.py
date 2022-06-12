from typing import Optional, Dict

from commons.daos.json_index import JsonIndexModel as Model


class TouchPoint(Model):
    is_complete: Optional[int]


class Recruiter(Model):
    name: Optional[str]
    username: Optional[str]
    company: Optional[str]
    headline: Optional[str]
    touchpoints: Optional[Dict[str, Optional[TouchPoint]]]
