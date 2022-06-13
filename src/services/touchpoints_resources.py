from ..data.models import TouchPoint
from ..resources import touchpoints

def build_touchpoints_schema():
    return {touchpoint: TouchPoint() for touchpoint in touchpoints}
