from starlette import status
from src.api.app import app
from src.data.indices import company_index


@app.get('/companies', status_code=status.HTTP_200_OK)
def get_companies():
    return [company for company in company_index.source.values()]


@app.get('/companies/next', status_code=status.HTTP_200_OK)
def get_companies_to_target_next(return_count: int = 5):
    for name, company in company_index.items():
        pass

