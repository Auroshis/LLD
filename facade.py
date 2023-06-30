"""
FACADE PATTERN is a structural pattern. It provides an unified interface to encapsulate all the subprocess or subsystems.
It provides the client a simpliflied interface while you can follow loose coupling, SOLID principles in background.
"""

# Complex subsystem classes
class Subsystem1:
    def operation1(self):
        print("Subsystem1 operation")

class Subsystem2:
    def operation2(self):
        print("Subsystem2 operation")

class Subsystem3:
    def operation3(self):
        print("Subsystem3 operation")


# Facade class
class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()
        self.subsystem3 = Subsystem3()

    def operation(self):
        # Facade provides a simplified interface to the subsystem
        self.subsystem1.operation1()
        self.subsystem2.operation2()
        self.subsystem3.operation3()


# Client code
facade = Facade()
facade.operation()
