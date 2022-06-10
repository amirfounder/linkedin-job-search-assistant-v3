from commons.daos.json_index import BaseJsonIndexModel, AbstractJsonIndexModel
from commons.helpers.classes import TypeRegistry


registry = TypeRegistry()


class TouchPoint(BaseJsonIndexModel):
    value = Key(int, None)
    metadata = Key(int, {})


class TouchPoint(BaseJsonIndexModel):
    def __init__(self, value=False, metadata=None, **kwargs):
        super().__init__(**kwargs)
        self.value = this_if_none(value, False)
        self.metadata = this_if_none(metadata, {})


class TouchPoints(AbstractJsonIndexModel):
    def __init__(self, **kwargs):
        self.initial_connection = None
        self.initial_connection_accepted = None

        assign_kwargs(self, kwargs, include_base=False)

        self.initial_connection = TouchPoint(kwargs.get('initial_connection'))
        self.initial_connection_accepted = TouchPoint(kwargs.get('initial_connection_accepted'))
        self.post_connection_intro_message = TouchPoint(kwargs.get('post_connection_intro_message'))
        self.post_connection_follow_up_message = TouchPoint(kwargs.get('post_connection_follow_up_message'))
        self.first_response = TouchPoint(kwargs.get(kwargs.get('first_response')))
        self.resume_sent = TouchPoint()
