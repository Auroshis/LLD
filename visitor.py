from abc import ABC, abstractmethod

# Visitor Interface
class ShoppingCartVisitor(ABC):
    @abstractmethod
    def visit_product(self, product):
        pass

    @abstractmethod
    def visit_discounted_product(self, discounted_product):
        pass

# Concrete Visitor
class PriceCalculator(ShoppingCartVisitor):
    def visit_product(self, product):
        return product.price

    def visit_discounted_product(self, discounted_product):
        return discounted_product.price - discounted_product.discount

# Element Interface
class ShoppingCartItem(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Concrete Element - Product
class Product(ShoppingCartItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        return visitor.visit_product(self)

# Concrete Element - Discounted Product
class DiscountedProduct(ShoppingCartItem):
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def accept(self, visitor):
        return visitor.visit_discounted_product(self)

# Object Structure - Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total_price(self, visitor):
        total_price = 0
        for item in self.items:
            total_price += item.accept(visitor)
        return total_price

# Client Code
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(Product("Item 1", 50))
    cart.add_item(Product("Item 2", 30))
    cart.add_item(DiscountedProduct("Discounted Item", 100, 20))

    price_calculator = PriceCalculator()
    total_price = cart.calculate_total_price(price_calculator)
    print(f"Total Price: ${total_price}")
