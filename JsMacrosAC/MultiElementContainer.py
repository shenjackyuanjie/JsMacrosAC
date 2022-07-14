from .OverlayContainer import *
from .IContainerParent import *
from .IOverlayParent import *


class MultiElementContainer(DrawableHelper, IContainerParent):
    parent: T = None
    x: int = None
    y: int = None
    width: int = None
    height: int = None

    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, parent: T, ):
        pass

    def init(self, ) -> None:
        pass

    def getVisible(self, ) -> bool:
        pass

    def setVisible(self, visible: bool, ) -> None:
        pass

    def addDrawableChild(self, drawableElement: T, ) -> T:
        pass

    def getButtons(self, ) -> list:
        pass

    def setPos(self, x: int, y: int, width: int, height: int, ) -> None:
        pass

    def openOverlay(self, overlay: OverlayContainer, ) -> None:
        pass

    def openOverlay(self, overlay: OverlayContainer, disableButtons: bool, ) -> None:
        pass

    def remove(self, button: Element, ) -> None:
        pass

    def getFirstOverlayParent(self, ) -> IOverlayParent:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    pass
