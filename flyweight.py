"""
The Flyweight design pattern is a structural design pattern that focuses on minimizing 
the memory usage of objects by sharing as much data as possible with other similar objects. It is often used when a large number of objects need to be created 
and their individual states can be extrinsic (context-dependent) or intrinsic (shared).
"""
class Flyweight:
    def __init__(self, shared_data):
        self.shared_data = shared_data

    def operation(self, extrinsic_data):
        # Perform operations using both shared and extrinsic data
        print(f"Shared data: {self.shared_data}, Extrinsic data: {extrinsic_data}")


class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = Flyweight(key)
        return self.flyweights[key]


factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("A")
flyweight1.operation("Data 1")  # Output: Shared data: A, Extrinsic data: Data 1

flyweight2 = factory.get_flyweight("B")
flyweight2.operation("Data 2")  # Output: Shared data: B, Extrinsic data: Data 2

# The next line will reuse the existing flyweight object for key "A"
flyweight3 = factory.get_flyweight("A")
flyweight3.operation("Data 3")  # Output: Shared data: A, Extrinsic data: Data 3
