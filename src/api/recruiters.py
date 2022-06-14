from typing import Dict

from commons.helpers import now

from fastapi import HTTPException, APIRouter
from src.data.indices import recruiter_index, company_index
from src.data.models import Recruiter, TouchPoint, Profile, Interaction, Company
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

    if not recruiter.touchpoints:
        recruiter.touchpoints = build_touchpoints_schema()

    recruiter_index[recruiter.username] = recruiter

    company_name = recruiter.profile.company
    if company_name not in company_index:
        company_index[company_name.lower().replace(' ', '_')] = Company(name=company_name)

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

    touchpoints_updated = []

    for name, touchpoint in touchpoints.items():
        if touchpoint.value is not recruiter.touchpoints[name].value:
            recruiter.touchpoints[name].value = touchpoint.value
            recruiter.touchpoints[name].updated_at = now()
            touchpoints_updated.append(name)

    recruiter_index.flush()

    if len(touchpoints_updated) > 0 and (company_key := recruiter.profile.company):
        interaction = Interaction()
        interaction.touchpoints_updated = touchpoints_updated
        interaction.recruiter_username = username

        company_key = company_key.lower().replace(' ', '_')

        if not (company := company_index.get(company_key)):
            company = Company()

        company.last_interaction = interaction
        company.interactions.insert(0, interaction)

        company_index.flush()

    return recruiter.dict()


@router.put('/{username}/profile', status_code=200)
def put_recruiter_profile(username: str, profile: Profile):
    if not (recruiter := recruiter_index.get(username)):
        raise HTTPException(status_code=404, detail="Recruiter does not exist. Create recruiter before updating.")

    recruiter.profile = profile
    return recruiter.dict()
