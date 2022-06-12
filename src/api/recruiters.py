from .app import app
from starlette import status
from src.data.indices import recruiter_index
from src.data.models import Recruiter


@app.get('/recruiters', status_code=status.HTTP_200_OK)
def get_recruiters():
    return [recruiter.json() for recruiter in recruiter_index.values()]


@app.get('/recruiters/{username}', status_code=status.HTTP_200_OK)
def get_recruiters_by_username(username: str):
    return recruiter_index.get(username)


@app.post('/recruiters', status_code=status.HTTP_201_CREATED)
def post_recruiter(recruiter: Recruiter):
    recruiter_index[recruiter.username] = recruiter
    return {recruiter.dict()}
