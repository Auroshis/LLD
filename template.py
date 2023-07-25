from abc import ABC, abstractmethod

# Abstract Class (Template)
class ReportTemplate(ABC):
    def generate_report(self):
        self.generate_header()
        self.generate_body()
        self.generate_footer()

    @abstractmethod
    def generate_header(self):
        pass

    @abstractmethod
    def generate_body(self):
        pass

    @abstractmethod
    def generate_footer(self):
        pass

# Concrete Class - Sales Report
class SalesReport(ReportTemplate):
    def generate_header(self):
        print("Sales Report Header")
        print("Date: July 2023")
        print("----------------------")

    def generate_body(self):
        print("Sales Data:")
        print("Product A - 100 units")
        print("Product B - 75 units")
        print("Product C - 150 units")

    def generate_footer(self):
        print("----------------------")
        print("Total Sales: $5000")

# Concrete Class - Inventory Report
class InventoryReport(ReportTemplate):
    def generate_header(self):
        print("Inventory Report Header")
        print("Date: July 2023")
        print("----------------------")

    def generate_body(self):
        print("Inventory Data:")
        print("Product A - 50 units")
        print("Product B - 25 units")
        print("Product C - 100 units")

    def generate_footer(self):
        print("----------------------")
        print("Total Inventory: 175 units")

# Client Code
if __name__ == "__main__":
    sales_report = SalesReport()
    inventory_report = InventoryReport()

    print("Generating Sales Report:")
    sales_report.generate_report()

    print("\nGenerating Inventory Report:")
    inventory_report.generate_report()
