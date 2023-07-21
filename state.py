"""
State design pattern is a behavioral pattern where the object changes it's state with
respect to internal state change.This pattern is particularly useful when an object's 
behavior changes significantly based on its internal state and avoids having large, conditional blocks
that handle different states, improving the code's readability and maintainability.
It's like a watcher.
"""
from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def action(self):
        pass

class StateA(State):
    """concrete class 1"""

    def action(self, context):
        print("State A action, followed by changing state to B")
        context.state = StateB()

class StateB(State):
    """concrete class 2"""
    
    def action(self, context):
        print("State B action, followed by changing state to A")
        context.state  = StateA()

class Context:
    state = None
    def __init__(self) -> None:
        self.state = StateA()
    
    def request(self):
        self.state.action(self)

# driver code
context = Context()
context.request()
context.request()
context.request()

