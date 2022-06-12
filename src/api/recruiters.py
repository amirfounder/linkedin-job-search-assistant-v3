from .app import app
from src.indices import recruiter_index
from ..models import Recruiter


@app.get('/recruiters')
def get_recruiters():
    recruiters = []
    for k, v in recruiter_index.source.items():
        recruiters.append(v.dict())
    return recruiters


@app.get('/recruiters/{username}')
def get_recruiters_by_username(username: str):
    return recruiter_index.get(username)


@app.post('/recruiters')
def post_recruiter(recruiter: Recruiter):
    recruiter_index[recruiter.username] = recruiter
    return recruiter.dict()
