from abc import ABC, abstractmethod

# Tweets demo for iterator pattern

class Iterator(ABC):
    """Abstract iterator method"""
    collection: list = []
    index = 0 # 1-indexed
    
    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass
        
    
class Aggregator(ABC):
    """Abstract method for aggregator"""
    collection: list = []
    @abstractmethod
    def createIterator(self):
        pass

# Concrete implementation

class Book:
    __name = ''
    __author = ''

    def __init__(self, name, author) -> None:
        self.__name = name
        self.__author = author
    
    def __getattr__(self, *args, **kwargs):
        return self.__name, self.__author

class BookIterator(Iterator):

    def __init__(self, books) -> None:
        self.collection = books

    def hasNext(self):
        return self.index < len(self.collection)
    
    def next(self):
        if self.hasNext():
            cur_book = self.collection[self.index]
            self.index += 1
            return cur_book.details
        else:
            raise StopIteration()
        
class Library(Aggregator):
    __books = list()
    def addBook(self, book:Book):
        self.__books.append(book)
    
    def createIterator(self):
        return BookIterator(self.__books)

# Driver Code

library = Library()
library.addBook(Book("System Design", "Alex Xu"))
library.addBook(Book("Mahabharat", "Ved Vyasa"))

iterator = library.createIterator()

while iterator.hasNext():
    print(iterator.next())

