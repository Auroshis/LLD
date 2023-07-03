"""
The Decorator design pattern is a structural design pattern that allows you to dynamically add new behavior or functionality to an 
existing object without modifying its structure. 
It involves creating a wrapper or decorator class that wraps around the original object and adds additional functionality.
"""
class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent operation")


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        super().operation()
        self.additional_operation()

    def additional_operation(self):
        print("ConcreteDecoratorA additional operation")


class ConcreteDecoratorB(Decorator):
    def operation(self):
        super().operation()
        self.extra_operation()

    def extra_operation(self):
        print("ConcreteDecoratorB extra operation")


# Usage example
component = ConcreteComponent()
decorator_a = ConcreteDecoratorA(component)
decorator_b = ConcreteDecoratorB(decorator_a)

decorator_b.operation()
