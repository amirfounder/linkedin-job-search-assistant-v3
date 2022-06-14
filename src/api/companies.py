from fastapi import APIRouter
from starlette import status
from src.data.indices import company_index

router = APIRouter(prefix='/companies')


@router.get('', status_code=status.HTTP_200_OK)
def get_companies():
    return [company for company in company_index.values()]


# Replace to queued instead of next
@router.get('/next', status_code=status.HTTP_200_OK)
def get_next_companies(return_count: int = 5):
    res = []
    for key, company in company_index.items():
        if len(res) >= return_count:
            break

        if not company.last_interaction:
            res.append((key, company))

    for key, company in res:
        company_index[key] = company_index.pop(key)

    res = [c for k, c in res]
    return res
