from commons.daos.json_index import BaseJsonIndexModel

from models.touchpoints import TouchPoints


class Recruiter(BaseJsonIndexModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.company = kwargs.get('company')
        self.headline = kwargs.get('headline')
        self.touchpoints = TouchPoints(kwargs.get('touchpoints'))
