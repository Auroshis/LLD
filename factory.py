"""
Factory Method is a Creational Design Pattern that allows an interface or a class to create an object,
but lets subclasses decide which class or object to instantiate. Using the Factory method, we have the
best ways to create an object. Here, objects are created without exposing the logic to the client,
and for creating the new type of object, the client uses the same common interface.

Advantages of using Factory method: 
We can easily add new types of products without disturbing the existing client code.
Generally, tight coupling is being avoided between the products and the creator classes and objects.
"""
from abc import ABC, abstractclassmethod

class RideSharing(ABC):
    """Abstract class for ridesharing subsclasses"""
    def __init__(self) -> None:
        pass
    
    @abstractclassmethod
    def getPrice(self):
        pass


class BikeSharing(RideSharing):
    """Concrete class for bike rentals"""
    def __init__(self) -> None:
        super().__init__()
    
    def getPrice(self):
        print("Bike will cost you Rs 10/Km")

class CarSharing(RideSharing):
    """Concrete class for car rentals"""
    def __init__(self) -> None:
        super().__init__()
    
    def getPrice(self):
        print("Car will cost you Rs 25/Km")

# Later adding Auto classes
class AutoSharing(RideSharing):
    """Concrete class for Auto rentals"""
    def __init__(self) -> None:
        super().__init__()
    
    def getPrice(self):
        print("Autowala will not stop for you haha!")

class SharingFactory:
    """Factory class to instantiate various ride sharing rentals"""
    __priceCatalog = {'Bike':BikeSharing,'Car':CarSharing, 'Auto': AutoSharing}

    @classmethod
    def getRide(cls, ride):
        """factor method to instantiate the desired ride by the client"""
        try:
            return cls.__priceCatalog[ride]()
        except KeyError:
            raise("Please give Bike/Car as option")

# driver code
# Client uses the same interface to instantiate different ride sharing objects
factory = SharingFactory()
carRide = factory.getRide('Car')
bikeRide = factory.getRide('Bike')

carRide.getPrice()
bikeRide.getPrice()

# After adding Auto
autoRide = factory.getRide('Auto')
autoRide.getPrice() 
