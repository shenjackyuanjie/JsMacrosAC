from .ItemStackHelper import *
from .BaseEvent import *


class EventItemDamage(Object, BaseEvent):
    item: ItemStackHelper = None
    damage: int = None

    def __init__(stack: ItemStack, damage: int, ):
        pass

    def toString(self, ) -> str:
        pass

    pass
