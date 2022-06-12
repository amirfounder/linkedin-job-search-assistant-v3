from typing import Dict

from .app import app
from fastapi import HTTPException
from src.data.indices import recruiter_index
from src.data.models import Recruiter, TouchPoint


@app.get('/recruiters', status_code=200)
def get_recruiters():
    return [recruiter.dict() for recruiter in recruiter_index.values()]


@app.get('/recruiters/{username}', status_code=200)
def get_recruiters_by_username(username: str):
    return recruiter_index.get(username)


@app.post('/recruiters', status_code=201)
def post_recruiter(recruiter: Recruiter):
    if recruiter.username in recruiter_index:
        raise HTTPException(status_code=400, detail="Recruiter already exists.")

    recruiter_index[recruiter.username] = recruiter
    return recruiter.dict()


@app.put('/recruiters/{username}/touchpoints', status_code=200)
def put_recruiter_touchpoints(username: str, touchpoints: Dict[str, TouchPoint]):
    recruiter = recruiter_index.get(username)

    if username not in recruiter_index:
        raise HTTPException(status_code=404, detail="Recruiter does not exist. Create recruiter before updating.")

    for name, touchpoint in touchpoints:
        recruiter.touchpoints[name] = touchpoint
