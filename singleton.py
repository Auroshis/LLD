"""
CATEGORY - CREATIONAL
 - To limit concurrent access to a shared resource.
 - To create a global point of access for a resource.
 - To create just one instance of a class, throughout the lifetime of a program.

 Use cases of a Singleton:
    Managing a database connection
    Global point access to writing log messages
    File Manager
    Print spooler
"""
class Logger:
    """Singleton class used for logging"""

    # Singleton instance
    __obj = None

    def __init__(self) -> None:
        if Logger.__obj != None:
            raise Exception("Use getInstance to use the Singleton object")
        else:
            Logger.__obj = self

    @staticmethod
    def getInstance():
        if Logger.__obj == None:
            Logger()
        return Logger.__obj
    
    def logMessage(self, msg):
        print(msg)

# Driver Code
log_obj1  = Logger.getInstance()

log_obj1.logMessage("Printing via log_obj1")

log_obj2 = Logger.getInstance()

log_obj2.logMessage("Printing from log_obj2")

print("is log_obj1 same as log_obj2 ->", log_obj1 == log_obj2)

print("location of log_obj1", id(log_obj1))
print("location of log_obj2", id(log_obj2))