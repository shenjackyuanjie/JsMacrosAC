from .Mappings import *
from .BaseLibrary import *


class FReflection(BaseLibrary, ):

    def getClass(self, name: str, ) -> object:
        pass

    def getClass(self, name: str, name2: str, ) -> object:
        pass

    def getDeclaredMethod(self, c: object, name: str, parameterTypes: object, ) -> Method:
        pass

    def getDeclaredMethod(self, c: object, name: str, name2: str, parameterTypes: object, ) -> Method:
        pass

    def getDeclaredField(self, c: object, name: str, ) -> Field:
        pass

    def getDeclaredField(self, c: object, name: str, name2: str, ) -> Field:
        pass

    def invokeMethod(self, m: Method, c: Object, objects: Object, ) -> Object:
        pass

    def newInstance(self, c: object, objects: Object, ) -> T:
        pass

    def loadJarFile(self, file: str, ) -> bool:
        pass

    def loadCurrentMappingHelper(self, ) -> Mappings:
        pass

    def getClassName(self, o: Object, ) -> str:
        pass

    def loadMappingHelper(self, urlorfile: str, ) -> Mappings:
        pass

    pass
