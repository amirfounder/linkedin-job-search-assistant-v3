from .app import app
from src.indices import company_index


@app.get('/companies')
def get_companies():
    return [company for company in company_index.source.values()]


@app.get('/companies/next')
def get_companies_to_target_next(return_count: int = 5):
    for name, company in company_index.source.items():
        pass

