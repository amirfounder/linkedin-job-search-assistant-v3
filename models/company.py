from datetime import datetime

from commons.daos import JsonIndexModel


class Company(JsonIndexModel):
    name: str
    last_connected: datetime
