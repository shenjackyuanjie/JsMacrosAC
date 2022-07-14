from JsMacrosAC.ItemStackHelper import *
from JsMacrosAC.BaseEvent import *


class EventArmorChange(Object, BaseEvent):
    slot: str = None
    item: ItemStackHelper = None
    oldItem: ItemStackHelper = None

    def __init__(slot: str, item: ItemStack, old: ItemStack, ):
        pass

    def toString(self, ) -> str:
        pass

    pass
