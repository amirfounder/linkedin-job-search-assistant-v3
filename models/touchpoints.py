from typing import Optional
from commons.daos import JsonIndexModel


class TouchPoint(JsonIndexModel):
    is_complete: int


class TouchPoints(JsonIndexModel):
    initial_connection: Optional[TouchPoint]
    initial_connection_accepted: Optional[TouchPoint]
    post_connection_intro_message: Optional[TouchPoint]
    post_connection_follow_up_message: Optional[TouchPoint]
    first_response: Optional[TouchPoint]
    resume_sent: Optional[TouchPoint]
