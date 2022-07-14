
class ConfigManager(Object, ):

    optionClasses: list = None
    options: list = None
    configFolder: File = None
    macroFolder: File = None
    configFile: File = None
    LOGGER: Logger = None
    rawOptions: JsonObject = None


    def __init__(configFolder: File, macroFolder: File, logger: Logger, ):
        pass


    def reloadRawConfigFromFile(self, ) -> None:
        pass

    def convertConfigFormat(self, ) -> None:
        pass

    def convertConfigFormat(self, clazz: object, ) -> None:
        pass

    def getOptions(self, optionClass: object, ) -> T:
        pass

    def addOptions(self, key: str, optionClass: object, ) -> None:
        pass

    def loadConfig(self, ) -> None:
        pass

    def loadDefaults(self, ) -> None:
        pass

    def saveConfig(self, ) -> None:
        pass


    pass
