from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .recruiters import router as recruiters
from .resources import router as resources

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recruiters, tags=['recruiters'])
app.include_router(resources, tags=['resources'])
