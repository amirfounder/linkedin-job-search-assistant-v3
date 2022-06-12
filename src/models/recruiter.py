from typing import Optional

from commons.daos.json_index import JsonIndexModel as Model


class TouchPoint(Model):
    is_complete: Optional[int]


class TouchPoints(Model):
    initial_connection: Optional[TouchPoint]
    initial_connection_accepted: Optional[TouchPoint]
    post_connection_intro_message: Optional[TouchPoint]
    post_connection_follow_up_message: Optional[TouchPoint]
    first_response: Optional[TouchPoint]
    resume_sent: Optional[TouchPoint]


class Recruiter(Model):
    name: Optional[str]
    username: Optional[str]
    company: Optional[str]
    headline: Optional[str]
    touchpoints: Optional[TouchPoints]
