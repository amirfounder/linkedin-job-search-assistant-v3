from commons.daos.json_index import BaseJsonIndexModel


class Company(BaseJsonIndexModel):
    def __init__(self, name, touchpoints, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.touchpoints = touchpoints
