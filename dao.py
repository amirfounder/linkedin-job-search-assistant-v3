from commons.daos.json_index import AbstractJsonIndex


class RecruiterIndex(AbstractJsonIndex):
    def __init__(self):
        super().__init__(
            source_path='data/recruiter_index.json',
            flush_after_put=True
        )

