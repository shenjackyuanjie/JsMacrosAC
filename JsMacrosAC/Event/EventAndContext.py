from JsMacrosAC.ContextContainer import *
from JsMacrosAC.BaseEvent import *


class EventAndContext(Object, ):
    event: BaseEvent = None
    context: ContextContainer = None

    def __init__(event: BaseEvent, context: ContextContainer, ):
        pass

    def toString(self, ) -> str:
        pass

    pass
