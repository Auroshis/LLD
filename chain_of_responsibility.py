"""
Chain of Responsibility method is Behavioral design pattern and it is the object-oriented
version of if … elif … elif … else and make us capable to rearrange the condition-action
blocks dynamically at the run-time. It allows us to pass the requests along the chain of
handlers. The processing is simple, whenever any handler received the request it has two
choices either to process it or pass it to the next handler in the chain. 
This pattern aims to decouple the senders of a request from its receivers by 
allowing the request to move through chained receivers until it is handled. 
"""

from abc import ABC

class HandlerInterface(ABC):
    """abstract class for handler of requests"""

    def __init__(self, next_handler) -> None:
        pass

    def handleLog(self, log_level, log_str):
        pass


class LogHandler(HandlerInterface):
    """Concrete handler class for handling logs"""

    __next_handler = None

    def __init__(self, next_handler) -> None:
        """Initializing next handler for current handler class"""
        self.__next_handler = next_handler
    
    def handleLog(self, log_level, log_str):
        if self.__next_handler:
            return self.__next_handler.handleLog(log_level, log_str)
        else:
            return False

class InfoHandler(LogHandler):
    def __init__(self, next_handler) -> None:
        super().__init__(next_handler)

    def handleLog(self, log_level, log_str):
        if log_level == 'INFO':
            print(log_str)
            return True
        else:
            return super().handleLog(log_level, log_str)

class DebugHandler(LogHandler):
    def __init__(self, next_handler) -> None:
        super().__init__(next_handler)

    def handleLog(self, log_level, log_str):
        if log_level == 'DEBUG':
            print(log_str)
            return True
        else:
            return super().handleLog(log_level, log_str)

class ErrorHandler(LogHandler):
    def __init__(self, next_handler) -> None:
        super().__init__(next_handler)

    def handleLog(self, log_level, log_str):
        if log_level == 'ERROR':
            print(log_str)
            return True
        else:
            return super().handleLog(log_level, log_str)

# client code

handler_obj = InfoHandler(DebugHandler(ErrorHandler(None)))

logs = [["WARNING", "you should not declare variabl......."], ["INFO", "vistor number xyz.."], ["DEBUG", "Value of x is,,.."], ["ERROR","keyError encounter at ....."]]

for loglvl, logstr in logs:
    response = handler_obj.handleLog(log_level=loglvl, log_str=logstr)
    if response:
        print("logged") 
    else:
        print("could not log")
