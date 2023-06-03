"""
Dependency Inversion states that High level classes should not interact directly with low level 
classes rather they should interact through abstractions.
"""

from abc import ABC, abstractmethod

class Datastore(ABC):
    """
    Abstract class for a key value data store.
    """
    @abstractmethod
    def push_data(self, key, value):
        pass

#low-level code
class Redis(Datastore):
    """
    Concrete class to put data into cache.
    """

    def push_data(self, key, value):
        # Data pushing code into cache
        print("Data pushed into cache successfully")

#low-level code
class DynamoDB(Datastore):
    """
    Concrete class to put data into database.
    """

    def push_data(self, key, value):
        # Data pushing code into data
        print("Data pushed into database successfully")


#high level code
class DataManager:
    """
    class to push data.
    """
    def __init__(self, datastore: Datastore) -> None:
        self.ds = datastore
    
    def push_data(self, key, value):
        """Method to push data into the selected datastore"""
        self.ds.push_data(key=key, value=value)


if __name__ == "__main__":
    database = DynamoDB()
    cache = Redis()
    
    # dynamically passing desired datastore obj as per the requirement
    cobj = DataManager(cache)
    cobj.push_data(key="Item", value="Apple")

    dobj = DataManager(database)
    dobj.push_data(key="Item", value="Orange")

        