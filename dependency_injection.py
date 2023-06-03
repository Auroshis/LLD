"""
Approach where we don't create objects of one class within another class to avoid tight coupling.
This principle helps in code modularity, maintainance & testability - unit tests and mocking.
"""
from abc import ABC, abstractmethod

class Database(ABC):
    """
    Abstract Database class.
    """
    def push_data(self, data):
        pass

class MongoDB(Database):
    """
    MongoDB database concrete class.
    """
    def __init__(self) -> None:
        print("Database connection initiated")
    
    def push_data(self, data):
        # data pushing code handled along with all edge cases
        print("Data pushing successful 200 OK", data)

class BackendFeature:
    """
    Concrete backend feature class
    """
    # constructor injection
    def __init__(self, connection: Database) -> None:
        self.db_connection = connection
    
    def add_user(self, user_data):
        # method to push user data into backend
        #user data validation before pushing along with raising validation error
        self.db_connection.push_data(data=user_data)

if __name__ == "__main__":
    mongo_connection = MongoDB()
    # dependency injection via constructor
    feature = BackendFeature(connection=mongo_connection)

    feature.add_user(user_data={"_id":"B317012", "name": "AUROSHIS"})