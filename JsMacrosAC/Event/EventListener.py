from JsMacrosAC.ScriptTrigger import *
from JsMacrosAC.Core import *
from JsMacrosAC.BaseListener import *
from JsMacrosAC.ContextContainer import *
from JsMacrosAC.BaseEvent import *


class EventListener(BaseListener, ):

    def __init__(macro: ScriptTrigger, runner: Core, ):
        pass

    def trigger(self, event: BaseEvent, ) -> ContextContainer:
        pass

    pass
