from abc import ABC, abstractmethod

class Mediator(ABC):
    """Abstract class for mediators"""
    @abstractmethod
    def addUser(self, colleague):
        pass
    @abstractmethod
    def removeUser(self, colleague):
        pass
    @abstractmethod
    def sendMessage(Self, colleague, message):
        pass

class Colleague(ABC):
    """Abstarct class for colleague"""
    @abstractmethod
    def setMediator(self, mediator):
        # TODO: Can you send messages to multiple mediators, you can customise with undo & other methods
        pass
    @abstractmethod
    def sendMessage(self, message):
        pass
    @abstractmethod
    def receiveMessage(self, message):
        pass

""" CHAT MEDIATOR IMPLEMENTATION """

class ChatMediator(Mediator):
    """Concrete class chat mediator implementation"""
    __users = []

    def addUser(self, user):
        # check for existing user
        self.__users.append(user)

    def removeUser(self, user):
        # check if user exists 
        self.__users.remove(user)
    
    def sendMessage(self, sender, message):
        #fan-out
        for receiver in self.__users:
            if receiver != sender:
                receiver.receiveMessage(message, sender)
        return True
    
class User(Colleague):
    """Concrete implementation of an user"""
    __name = ''
    __mediator: Mediator = None

    def __init__(self, name) -> None:
        self.__name = name

    def __getattr__(self, *args, **kwargs):
        return self.__name
    
    def setMediator(self, mediator):
        self.__mediator = mediator
        return True
    
    def sendMessage(self, message):
        self.__mediator.sendMessage(self, message)
    
    def receiveMessage(self, message, sender):
        print("{0} - {1}".format(message, sender.name))


""" DRIVER CODE"""
# creating chat mediator and users
Chat = ChatMediator()

user1 = User("John")
user2 = User("Rock")

# setting mediator & users in a group structure
user1.setMediator(Chat)
user2.setMediator(Chat)

Chat.addUser(user1)
Chat.addUser(user2)

# fun part
user2.sendMessage("Hi! welcome to the group")
user1.sendMessage("Hey there!! I hope you all are having a good time")