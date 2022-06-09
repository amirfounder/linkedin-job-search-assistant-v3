from commons.daos.json_index import AbstractJsonIndexModel


class Recruiter(AbstractJsonIndexModel):
    def __init__(self, name, company, headline):
        super().__init__()
        self.name = name
        self.company = company
        self.headline = headline
