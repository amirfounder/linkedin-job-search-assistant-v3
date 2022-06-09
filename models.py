from commons.daos.json_index import AbstractJsonIndexModel


class TouchPoints(AbstractJsonIndexModel):
    def __init__(self, **kwargs):
        super().__init__()
        self.initial_connection = InitialConnection(**kwargs.get('initial_connection'))


class InitialConnection(AbstractJsonIndexModel):
    def __init__(self, has_been_sent, timestamp_sent):
        super().__init__()
        self.has_been_sent = has_been_sent
        self.timestamp_sent = timestamp_sent


class Recruiter(AbstractJsonIndexModel):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.company = kwargs.get('company')
        self.headline = kwargs.get('headline')
        self.touchpoints = TouchPoints(**kwargs.get('touchpoints', {}))
