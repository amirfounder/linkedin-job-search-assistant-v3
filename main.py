from flask import Flask
from flask_cors import CORS

from dao import RecruiterIndex
from models import Recruiter


app = Flask(__name__)
CORS(app)
recruiters = RecruiterIndex()


@app.route('/', methods=['POST'])
def handle_request():
    pass


if __name__ == '__main__':
    r = Recruiter('hello', 'yes', 'this')
