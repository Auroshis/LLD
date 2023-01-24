"""
Strategy pattern is a behavioural design pattern 
which allows us to select algorithms/strategies during runtime.
"""
from abc import ABC

class DrivingStrategy(ABC):
    """abstarct base class for Driving strategies/algorithms"""

    def drive(self):
        print("Normal driving")

class OffroadStrategy(DrivingStrategy):
    """concrete class for off-road driving"""

    def drive(self):
        print("OfF ROad driving")

class F1Strategy(DrivingStrategy):
    """concrete class for F1 driving"""\
    
    def drive(self):
        print("F1 driving strategy")


class Vehicle(ABC):
    """abstract base class for Vehicle"""
    
    def __init__(self,strategy_obj) -> None:
        self.driving_strategy = strategy_obj
    
    def driveVehicle(self):
        self.driving_strategy.drive()

class Defender(Vehicle):
    """concrete class for Defender"""
    def __init__(self, strategy_obj) -> None:
        super().__init__(strategy_obj)
    
    def driveVehicle(self):
        return super().driveVehicle()

class FerrariGTB(Vehicle):
    """Concrete class for Ferrari GTB """
    def __init__(self, strategy_obj) -> None:
        super().__init__(strategy_obj)
    
    def driveVehicle(self):
        return super().driveVehicle()

offroad = OffroadStrategy()

defender = Defender(offroad)
defender.driveVehicle()

ferrari = FerrariGTB(F1Strategy())
ferrari.driveVehicle()