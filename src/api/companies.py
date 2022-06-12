from .app import app
from src.indices import company_index


@app.get('/')
def get_companies():
    pass
