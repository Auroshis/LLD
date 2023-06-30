from log_module.handlers import FileLogHandler, ConsoleLogHandler

class Logger:
    """
    Concrete class to add logs.
    """
    __instance = None
    __console = ConsoleLogHandler()
    __file = FileLogHandler()

    def __init__(self) -> None:
        # Singleton Pattern
        if Logger.__instance == None:
            Logger.__instance = self
        
    def addLog(self, msg, level, handler):
        if handler == "Console":
            self.__console.logMessage(msg=msg, level=level)
        elif handler == "File":
            self.__file.logMessage(msg=msg, level=level)
        