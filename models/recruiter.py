from commons.daos.json_index import JsonIndexModel as Model

from models.touchpoints import TouchPoints


class Recruiter(Model):
    name: str
    username: str
    company: str
    headline: str
    touchpoints: TouchPoints
