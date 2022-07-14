from JsMacrosAC.PlayerListEntryHelper import *
from JsMacrosAC.BaseEvent import *


class EventPlayerLeave(Object, BaseEvent):
    UUID: str = None
    player: PlayerListEntryHelper = None

    def __init__(uuid: UUID, player: PlayerListEntry, ):
        pass

    def toString(self, ) -> str:
        pass

    pass
