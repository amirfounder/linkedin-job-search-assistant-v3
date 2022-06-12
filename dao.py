from commons.daos.json_index import JsonIndex

from models import Recruiter, Company


class RecruiterIndex(JsonIndex[str, Recruiter]):
    _source_path = 'data/recruiter_index.json'
    _flush_after_set = True


class CompanyIndex(JsonIndex[str, Company]):
    _source_path = 'data/company_index.json'
    _flush_after_set = True

