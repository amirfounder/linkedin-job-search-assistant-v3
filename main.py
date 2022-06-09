from http import HTTPStatus

from flask import Flask, request
from flask_cors import CORS

from dao import RecruiterIndex
from models import Recruiter


app = Flask(__name__)
CORS(app)
index = RecruiterIndex()


@app.route('/recruiters/save', methods=['POST'])
def handle_request():
    profile = request.json
    username = profile['username']
    recruiter = Recruiter(**profile)
    index.put(username, dict(recruiter))

    return 'OK', HTTPStatus.OK


if __name__ == '__main__':
    app.run(port=8082)

