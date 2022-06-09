from abc import ABC

from commons.daos.json_index import BaseJsonIndexModel, AbstractJsonIndexModelsDict
from commons.helpers.case_conversion import pascal_to_snake
from commons.helpers.classes import TypeRegistry


registry = TypeRegistry()


class AbstractTouchPoint(BaseJsonIndexModel, ABC):
    def __init__(self, status: str = 'N/A', **kwargs):
        super().__init__(**kwargs)
        self.status = status

    def __init_subclass__(cls, **kwargs):
        key = pascal_to_snake(cls.__name__)
        registry[key] = cls


class TouchPoints(AbstractJsonIndexModelsDict):
    def __init__(self, source=None):
        super().__init__(source)
        for key, value in self.source.items():
            if key in registry:
                self.source[key] = registry[key](**value)


class InitialConnection(AbstractTouchPoint):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class InitialConnectionAccepted(AbstractTouchPoint):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PostConnectionIntroductionMessage(AbstractTouchPoint):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PostConnectionFollowUpMessage(AbstractTouchPoint):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
