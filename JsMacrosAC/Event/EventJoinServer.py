from JsMacrosAC.ClientPlayerEntityHelper import *
from JsMacrosAC.BaseEvent import *


class EventJoinServer(Object, BaseEvent):
    player: ClientPlayerEntityHelper = None
    address: str = None

    def __init__(player: ClientPlayerEntity, address: str, ):
        pass

    def toString(self, ) -> str:
        pass

    pass
