from JsMacrosAC.ItemStackHelper import *
from JsMacrosAC.BaseEvent import *


class EventItemDamage(Object, BaseEvent):
    item: ItemStackHelper = None
    damage: int = None

    def __init__(stack: ItemStack, damage: int, ):
        pass

    def toString(self, ) -> str:
        pass

    pass
