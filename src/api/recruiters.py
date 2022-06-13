from typing import Dict

from commons.helpers import now

from fastapi import HTTPException, APIRouter
from src.data.indices import recruiter_index
from src.data.models import Recruiter, TouchPoint, Profile
from src.services.touchpoints_resources import build_touchpoints_schema

router = APIRouter(prefix='/recruiters')


@router.get('', status_code=200)
def get_recruiters():
    return [recruiter.dict() for recruiter in recruiter_index.values()]


@router.get('/{username}', status_code=200)
def get_recruiters_by_username(username: str):
    return recruiter_index.get(username)


@router.get('/{username}/exists', status_code=200)
def get_recruiters_does_exist(username: str):
    return username in recruiter_index


@router.post('', status_code=201)
def post_recruiter(recruiter: Recruiter):
    if recruiter.username in recruiter_index:
        raise HTTPException(status_code=400, detail="Recruiter already exists.")

    recruiter.touchpoints = build_touchpoints_schema()
    recruiter_index[recruiter.username] = recruiter
    return recruiter.dict()


@router.get('/{username}/touchpoints', status_code=200)
def get_recruiter_touchpoints(username: str):
    if not (recruiter := recruiter_index.get(username)):
        raise HTTPException(status_code=404, detail="Recruiter does not exist. Create recruiter before getting.")

    return recruiter.touchpoints


@router.put('/{username}/touchpoints', status_code=200)
def put_recruiter_touchpoints(username: str, touchpoints: Dict[str, TouchPoint]):
    if not (recruiter := recruiter_index.get(username)):
        raise HTTPException(status_code=404, detail="Recruiter does not exist. Create recruiter before updating.")

    for name, touchpoint in touchpoints.items():
        if touchpoint.value is not recruiter.touchpoints[name].value:
            recruiter.touchpoints[name].value = touchpoint.value
            recruiter.touchpoints[name].updated_at = now()

    recruiter_index.flush()
    return recruiter.dict()


@router.put('/{username}/profile', status_code=200)
def put_recruiter_profile(username: str, profile: Profile):
    if not (recruiter := recruiter_index.get(username)):
        raise HTTPException(status_code=404, detail="Recruiter does not exist. Create recruiter before updating.")

    recruiter.profile = profile
    return recruiter.dict()
