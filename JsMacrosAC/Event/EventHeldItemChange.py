from JsMacrosAC.ItemStackHelper import *
from JsMacrosAC.BaseEvent import *


class EventHeldItemChange(Object, BaseEvent):
    offHand: bool = None
    item: ItemStackHelper = None
    oldItem: ItemStackHelper = None

    def __init__(item: ItemStack, oldItem: ItemStack, offHand: bool, ):
        pass

    def toString(self, ) -> str:
        pass

    pass
