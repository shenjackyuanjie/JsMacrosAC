from .BaseEvent import *
from .Core import *
from .ContextContainer import *
from .BaseListener import *
from .ScriptTrigger import *

class EventListener(BaseListener, ):



    def __init__(macro: ScriptTrigger, runner: Core, ):
        pass


    def trigger(self, event: BaseEvent, ) -> ContextContainer:
        pass


    pass
