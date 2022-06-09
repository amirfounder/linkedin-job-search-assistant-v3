from datetime import timedelta
from http import HTTPStatus

from commons import now, safe_cast
from flask import Flask, request
from flask_cors import CORS

from dao import RecruiterIndex, CompanyIndex
from models import Recruiter, Company

app = Flask(__name__)
CORS(app)

recruiters_idx = RecruiterIndex()
companies_idx = CompanyIndex()


@app.route('/recruiters/save', methods=['POST'])
def save_recruiter():
    profile = request.json
    username = profile['username']
    company_name = profile.get('company')

    recruiter = Recruiter(**profile)
    recruiters_idx.put(username, dict(recruiter))

    if company_name:
        company = companies_idx.get(company_name)
        if not company:
            company = Company(company_name)
        else:
            for _, touchpoint in recruiter.touchpoints:
                if company.updated_at < touchpoint.updated_at:
                    company.updated_at = touchpoint.updated_at
        companies_idx.put(company_name, company)

    return 'SUCCESS', HTTPStatus.CREATED


@app.route('/recruiters/<username>', methods=['GET'])
def get_recruiters(username):
    source = recruiters_idx.source
    resp = source[username] if username else dict(source)
    return resp, HTTPStatus.OK


@app.route('/companies/next', methods=['GET'])
def get_next_search_query():
    hours_interval = safe_cast(request.args.get('hours'), int, False, 24)

    for company in companies_idx:
        if company.updated_at < now() - timedelta(hours=hours_interval):
            return company, HTTPStatus.OK


if __name__ == '__main__':
    app.run(port=8082)

