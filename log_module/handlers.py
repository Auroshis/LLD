import logging
from abc import ABC

class LogHandler(ABC):
    """
    Abstract class for log handler.
    """
    def logMessage(self, msg, level):
        pass

class BaseLogHandler(LogHandler):
    """
    Concrete class for base log handler
    """
    _logger = None
    _formatter = None

    def __init__(self) -> None:
        # Create a logger
        self._logger = logging.getLogger('simple_logger')
        self._logger.setLevel(logging.INFO)  # Set the overall log level
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    def logMessage(self, msg, level):
        # This can be implemented using Chain of responsibility pattern
        if level == "DEBUG":
            self._logger.debug(msg=msg)
        elif level == "ERROR":
            self._logger.error(msg=msg)
        elif level == "WARNING":
            self._logger.warning(msg=msg)
        elif level == "CRITICAL":
            self._logger.critical(msg=msg)
    
class ConsoleLogHandler(BaseLogHandler):
    """
    Concrete class for console log handler.
    """

    def __init__(self) -> None:
        super().__init__()
        console_handler = logging.StreamHandler()  # Log to console
        console_handler.setFormatter(self._formatter)
        self._logger.addHandler(console_handler)
    
    
class FileLogHandler(BaseLogHandler):
    """
    Concrete class for File log handler.
    """

    def __init__(self) -> None:
        super().__init__()
        file_handler = logging.FileHandler("general.log")  # Log to console
        file_handler.setFormatter(self._formatter)
        self._logger.addHandler(file_handler)
        file_handler.setLevel(logging.WARNING)
    
# TODO : MAKE 2 DIFFERENT LOGGER FOR DIFFERENT HANDLERS..SAME OBJECT IS GETTING OVERRIDDEN
