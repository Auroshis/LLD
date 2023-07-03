"""
The Composite design pattern is a structural design pattern that allows you to compose objects into tree-like structures and work with them 
as if they were individual objects. 
This pattern is useful when you have a hierarchical structure of objects and want to treat individual objects and groups of objects uniformly.
"""
class Component:
    def draw(self):
        pass


class Button(Component):
    def draw(self):
        print("Drawing a button")


class Panel(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def draw(self):
        print("Drawing a panel")
        for child in self.children:
            child.draw()


# Usage example
button1 = Button()
button2 = Button()

panel = Panel()
panel.add(button1)
panel.add(button2)

panel.draw()
