from datetime import datetime
from typing import Optional

from commons.daos import JsonIndexModel


class Company(JsonIndexModel):
    name: str
    last_connected: Optional[datetime]
