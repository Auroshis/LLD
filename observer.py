"""
CATEGORY - BEHAVIOURAL
The observer method is a Behavioral design Pattern which allows you to define or create a subscription mechanism to send the notification 
to the multiple objects about any new event that happens to the object that they are observing. The subject is basically observed by multiple
objects. The subject needs to be monitored and whenever there is a change in the subject, the observers are being notified about the change. 
This pattern defines one to Many dependencies between objects so that one object changes state, all of its dependents are notified and
updated automatically.

Problem it solves - You can push updates in an targeted fashion without subscribers worrying about checking the latest updates themselves
"""
# Newsletter example
from abc import ABC, abstractclassmethod

class NewsLetter(ABC):
    """Abstract class for newsletter"""
    def __init__(self) -> None:
        pass
    
    @abstractclassmethod
    def addSubscriber(self):
        pass

    @abstractclassmethod
    def removeSubscriber(self):
        pass

    @abstractclassmethod
    def publishNews(self):
        pass

class DelhiTimes(NewsLetter):
    """Concrete newsletter class for DelhiTimes"""
    __name = "DelhiTimes"
    __subs = []
    def __init__(self) -> None:
        super().__init__()

    @classmethod    
    def addSubscriber(cls, subscriber):
        if subscriber in cls.__subs:
            print("Already Subsribed")
        else:
            cls.__subs.append(subscriber)
            print("{0} successfully subscribed to DelhiTimes".format(subscriber.getName()))
    
    @classmethod
    def removeSubscriber(cls, subscriber):
        if subscriber in cls.__subs:
            cls.__subs.remove(subscriber)
            print("{0} unsubscribed successfully from DelhiTimes".format(subscriber.getName()))
        else:
            print("Subsriber doesn't exist")
    
    @classmethod
    def publishNews(cls, news):
        for subscriber in cls.__subs:
            subscriber.receiveUpdate(news, cls.__name)

class DalalStreetJournal(NewsLetter):
    """Concrete newsletter class for DalalStreetJournal"""
    __name = "DalalStreetJournal"
    __subs = []
    def __init__(self) -> None:
        super().__init__()

    @classmethod    
    def addSubscriber(cls, subscriber):
        if subscriber in cls.__subs:
            print("Already Subsribed")
        else:
            cls.__subs.append(subscriber)
            print("{0} successfully subscribed to DalalStreetJournal".format(subscriber.getName()))
    
    @classmethod
    def removeSubscriber(cls, subscriber):
        if subscriber in cls.__subs:
            cls.__subs.remove(subscriber)
            print("{0} unsubscribed successfully from DalalStreetJournal".format(subscriber.getName()))
        else:
            print("Subsriber doesn't exist")
    
    @classmethod
    def publishNews(cls, news):
        for subscriber in cls.__subs:
            subscriber.receiveUpdate(news, cls.__name)

"""----------------------------------SECTION BREAK---------------------------------------------------"""

class Subscriber:
    """Concrete class for Subsriber"""
    def __init__(self, name) -> None:
        self.__name = name
    
    def getName(self):
        #getter method to get name
        return self.__name

    def receiveUpdate(self, news, source):
        print("News Update from {2} for {0}\n{1}".format(self.__name, news, source))

# Driver code

# create 2 subs and subscribe the newsletter in different combinations

Auroshis = Subscriber('Auroshis')
Subhojit = Subscriber('Subhojit')

# Adding Subscriptions

DelhiTimes.addSubscriber(Auroshis)
DalalStreetJournal.addSubscriber(Auroshis)
DalalStreetJournal.addSubscriber(Subhojit)

# pushing updates
DelhiTimes.publishNews("Ben Stokes sold for 16.25Cr INR to Chennai Super Kings...")
DalalStreetJournal.publishNews("NIFTY down by 1.25% amid rise in COVID cases...")

# after removing a subscriber
DalalStreetJournal.removeSubscriber(Auroshis)

DelhiTimes.publishNews("MS Dhoni renewed his contract with CSK till 2025...")
DalalStreetJournal.publishNews("NASDAQ down by 7% due to war escalations in Ukraine... ")







