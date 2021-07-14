from .ScriptTrigger import *
from .BaseWrappedException import *
from .LibraryRegistry import *
from .BaseEventRegistry import *
from .BaseProfile import *
from .BaseEvent import *
from .BaseLanguage import *
from .ContextContainer import *
from .ConfigManager import *

class Core(Object, ):

    instance: self = None
    eventRegistry: BaseEventRegistry = None
    profile: BaseProfile = None
    config: ConfigManager = None
    libraryRegistry: LibraryRegistry = None
    contexts: list = None
    threadContext: list = None
    languages: list = None
    defaultLang: BaseLanguage = None


    def createInstance(self, eventRegistryFunction: Function, profileFunction: Function, configFolder: File, macroFolder: File, logger: Logger, ) -> self:
        pass

    def addLanguage(self, l: BaseLanguage, ) -> None:
        pass

    def sortLanguages(self, ) -> None:
        pass

    def exec(self, macro: ScriptTrigger, event: BaseEvent, ) -> ContextContainer:
        pass

    def exec(self, macro: ScriptTrigger, event: BaseEvent, then: Runnable, catcher: Consumer, ) -> ContextContainer:
        pass

    def wrapException(self, ex: Throwable, ) -> BaseWrappedException:
        pass


    pass
