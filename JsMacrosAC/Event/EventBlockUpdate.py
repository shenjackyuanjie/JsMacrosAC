from JsMacrosAC.BlockDataHelper import *
from JsMacrosAC.BaseEvent import *


class EventBlockUpdate(Object, BaseEvent):
    block: BlockDataHelper = None
    updateType: str = None

    def __init__(block: BlockState, blockEntity: BlockEntity, blockPos: BlockPos, updateType: str, ):
        pass

    def toString(self, ) -> str:
        pass

    pass
