import uvicorn
from datetime import timedelta
from http import HTTPStatus

from commons.helpers import now
from commons.utils import safe_cast
from flask import Flask, request
from flask_cors import CORS

from indices import RecruiterIndex, CompanyIndex
from models import Recruiter, Company


recruiters_idx = RecruiterIndex.build()
companies_idx = CompanyIndex.build()


@app.route('/recruiters/save', methods=['POST'])
def save_recruiter():
    profile = request.json
    username = profile['username']
    company_name = profile.get('company')

    recruiter = Recruiter(**profile)
    recruiters_idx.put(username, dict(recruiter))

    if company_name:
        company_dict = companies_idx.get(company_name)
        company = Company(**company_dict) if company_dict else Company(name=company_name)

        for touchpoint in recruiter.touchpoints.get():
            if company.updated_at < touchpoint.updated_at:
                company.updated_at = touchpoint.updated_at
                break

        companies_idx.put(company_name, company)

    return 'SUCCESS', HTTPStatus.CREATED


@app.route('/recruiters/<username>', methods=['PUT'])
def update_recruiter(username):
    recruiter = recruiters_idx.get(username)


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


