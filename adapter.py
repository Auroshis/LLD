"""
STRUCTURAL PATTERN
Intro
Adapter method is a Structural Design Pattern which helps us in making the incompatible objects adaptable to each other.
The main purpose of this method is to create a bridge between two incompatible interfaces without the client having to make a lot of changes.

Advantages:-
- Principle of Single Responsibility: We can achieve the principle of Single responsibility with Adapter Method because here we can separate the concrete code from the primary logic of the client.
- Flexibility: Adapter Method helps in achieving the flexibility and reusability of the code.
- Less complicated class: Our client class is not complicated by having to use a different interface and can use polymorphism to swap between different implementations of adapters.
- Open/Closed principle: We can introduce the new adapter classes into the code without violating the Open/Closed principle.

Disadvantages:-
- Complexity of the Code: As we have introduced the set of new classes, objects and interfaces, the complexity of or code definitely rises.
- Adaptability: Most of the times, we require many adaptations with the adaptee chain to reach the compatibility what we want.

Applicability:-
- Consume legacy Code
- To make classes and interfaces compatible : Adapter method is always used when we are in need to make certain classes compatible to communicate.

Adaptee - uncompatible class/interface
Adapter - the target class used by the client
"""

# Example Code - Currency Converter

from abc import ABC, abstractclassmethod

class Currency(ABC):
    """Abstract currency class for currency"""
    __notation = ''
    def __init__(self) -> None:
        pass
    
    def getNotation(self):
        """Returns the currency notation"""
        pass

    def getMoney(self):
        pass

# Adaptee
class IndianCurrency(Currency):
    """Concrete class for Indian currency"""
    __notation = 'INR'
    def __init__(self, value) -> None:
        super().__init__()
        self.value_given = value
    
    @classmethod
    def getNotation(cls):
        return cls.__notation
    
    def getMoney(self):
        return self.value_given

# Adapter
class USACurrencyAdapter():
    """Concrete adapter class for USA Currency"""
    __notation = 'USD'
    __conversion_rate = {'INR':80}

    def __init__(self, currency) -> None:
        super().__init__()
        self.currency_given = currency
    
    @classmethod
    def getNotation(cls):
        return cls.__notation
    
    def getMoney(self):
        """converting the input currency to USD"""
        return self.currency_given.getMoney() / self.__conversion_rate[self.currency_given.getNotation()]

#------------------Buyer Class-------------------------------------------------

class Walmart:
    """Concrete class for shop"""
    __product_catalog = {'brush':8, 'pen':10, 'towels':10}
    def __init__(self) -> None:
        pass
    
    @classmethod
    def buyItem(cls, item, currency):
        if currency.getNotation() == 'USD':
            if not cls.__product_catalog[item]:
                raise ("Item does not exist!")
            else:
                if currency.getMoney() >= cls.__product_catalog[item]:
                    print("Succesfully Purchased!!")
                else:
                    print("Insufficient Balance!!")
        else:
            print("Sorry! We only accept USD.")


# ------------------------------------------------------driver code -----------------------------------------------------------

inr1 = IndianCurrency(900)
# using Adapter pattern
usd1 = USACurrencyAdapter(inr1)
shop = Walmart()

item1 = 'pen'
item2 = 'paper'

shop.buyItem(item=item1, currency=usd1)
shop.buyItem(item=item1, currency=inr1)

inr2 = IndianCurrency(90)
# using Adapter pattern
usd2 = USACurrencyAdapter(inr2)

shop.buyItem(item=item1, currency=usd2)
shop.buyItem(item=item1, currency=inr2)




