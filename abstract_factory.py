"""
Abstract Factory Method is a Creational Design pattern that allows you to produce the families of related objects without specifying
their concrete classes. Using the abstract factory method, we have the easiest ways to produce a similar type of many objects. 
Advantages of using Abstract Factory method:
 - This pattern is particularly useful when the client doesn’t know exactly what type to create. 
 - It is easy to introduce new variants of the products without breaking the existing client code.
 - Products which we are getting from the factory are surely compatible with each other.
Disadvantages of using Abstract Factory method:
 - Our simple code may become complicated due to the existence of a lot of classes.
 - We end up with a huge number of small files i.e, cluttering of files.
Applicability:
 - Most commonly, abstract factory method pattern is found in the sheet metal stamping equipment used in the manufacture of automobiles.
 - It can be used in a system that has to process reports of different categories such as reports related to input, output, and intermediate transactions.
"""

from abc import ABC

class VehicleFactory(ABC):
    """Abstract base class for various factories"""
    def build(self):
        pass

class CarFactory(VehicleFactory):
    """Concrete class to build cars"""
    def __init__(self) -> None:
        self.car = dict()
    
    def build(self, ecap, whls, brand):
        self.car['brand'] = brand
        self.car['wheels'] = whls
        self.car['engine_capacity'] = ecap
        return self.car

class TruckFactory(VehicleFactory):
    """Concrete class to build trucks"""
    def __init__(self) -> None:
        self.truck = dict()
    
    def build(self, ecap, whls, brand):
        self.truck['brand'] = brand
        self.truck['wheels'] = whls
        self.truck['engine_capacity'] = ecap
        return self.truck

class BrandFactory(ABC):
    """Abstract Base class for vehicle Brands"""
    def __init__(self) -> None:
        pass
    def returnVehicle(self):
        pass

class TataFactory(BrandFactory):
    """concrete class for TATA factory"""
    __brand_name = 'TATA'

    def returnVehicle(self, vehicle):
        """returns Vehicle object as requested by the customer"""
        if vehicle.lower() == 'car':
            car = CarFactory()
            return car.build('1200cc', '4X16inch', self.__brand_name)
        elif vehicle.lower() == 'truck':
            truck = TruckFactory()
            return truck.build('6000cc', '10X20nch', self.__brand_name)
        else:
            return "Bhai kahan agaya tu!!"

class MahindraFactory(BrandFactory):
    """concrete class for TATA factory"""
    __brand_name = 'MAHINDRA'

    def returnVehicle(self, vehicle):
        """returns Vehicle object as requested by the customer"""
        if vehicle.lower() == 'car':
            car = CarFactory()
            return car.build('1200cc', '4X16inch', self.__brand_name)
        elif vehicle.lower() == 'truck':
            truck = TruckFactory()
            return truck.build('6000cc', '10X20nch', self.__brand_name)
        else:
            return "Bhai kahan agaya tu!!"

class CarBuy:
    """concrete class for selling vehicles"""
    __brands = {'TATA':TataFactory, 'MAHINDRA':MahindraFactory}

    def getVehicle(self, brand, type):
        """static method to return the desired vehicle of desired brand to the customer"""
        try:
            brand_obj = self.__brands[brand]()
            vehicle = brand_obj.returnVehicle(type)
            return vehicle
        except KeyError:
            return "Please select an available brand"

# driver code
customer = CarBuy()
vehicle = customer.getVehicle('TATA', 'car')
print(vehicle)
vehicle = customer.getVehicle('MAHINDRA', 'car')
print(vehicle)

        