from commons.daos.json_index import JsonIndex

from .models import Recruiter, Company


recruiter_index = JsonIndex(Recruiter, 'data/recruiter_index.json', {'flush_after_set': True})
company_index = JsonIndex(Company, 'data/company_index.json', {'flush_after_set': True})
