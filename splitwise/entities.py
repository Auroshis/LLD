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


# class SplitStrategy(ABC):
#     """
#     Abstract class for creating splits
#     """
#     @abstractmethod
#     def split(self, split_ratios, total):
#         pass


class Expense:
    """Class representing an Expense"""
    __added_by : User
    __is_settled: bool = False
    __payment: Payment
    __splits: dict = {}
    __payments: dict = {}
    __image_url: str = ''

    def __init__(self, added_by, payment, currency) -> None:
        self.__added_by = added_by
        self.__payment = Payment(value=payment, currency=currency)
        
class ExpenseSplitter(ABC):
    """
    Abstract class for taking user input and splitting into ratios
    """
    __ratios: dict = {}
    
    @abstractmethod
    def splitPayment(self):
        pass