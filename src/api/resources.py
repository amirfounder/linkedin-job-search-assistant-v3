from fastapi import APIRouter

from ..resources import touchpoints
from ..services.touchpoints_resources import build_touchpoints_schema

router = APIRouter(prefix='/resources')


@router.get('/touchpoints')
def get_touchpoint_resources():
    return touchpoints


@router.get('/touchpoints/schema')
def get_touchpoint_schema_resources():
    return build_touchpoints_schema()
