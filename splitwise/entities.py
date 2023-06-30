from abc import ABC, abstractmethod


class User:
    """
    Class representing a single User.
    NOTE: User's name will be considered unique for simplicity.
    However, we can try some sort of UUID as well.
    """
    __name: str = ''
    __mail: str = ''
    __age: int = 0
    __friends: set = set()
    __balance_sheet: dict = {}

    def __init__(self, name, mail, age) -> None:
        self.__name = name
        self.__mail = mail
        self.__age = age

    def getName(self):
        return self.__name
    
    def getFriends(self):
        return self.__friends
    
    def setFriend(self, friend):
        self.__friends.add(friend)
        return True
    
    def removeFriend(self, friend):
        self.__friends.remove(friend)
        return True


class Payment:
    """
    Class representing a single payment entity.
    """
    # NOTE: A negative value represents you have to pay while a positive value suggests the reverse
    __currency : str
    __value: float

    def __init__(self, value, currency) -> None:
        self.__value = value
        self.__currency = currency
    
    def getValue(self):
        return self.__value, self.__currency


class Expense:
    """Class representing an Expense"""
    __added_by : User
    __title: str
    __is_settled: bool = False
    __total: Payment
    __splits: dict = {}
    __payments: dict = {}
    __image_url: str = ''
    __strategy:str = 'equal'

    def __init__(self, added_by, payment, currency, title, strategy) -> None:
        self.__added_by = added_by
        self.__total = Payment(value=payment, currency=currency)
        self.__title = title
        self.__strategy = strategy
    
    def setSplits(self, splits):
        self.__splits = splits
    
    def setPayments(self, payments):
        self.__payments = payments
    
    def getPayments(self):
        return self.__payments
    
    def getSplits(self):
        return self.__splits
    
    def getTotal(self):
        return self.__total.getValue()[0]