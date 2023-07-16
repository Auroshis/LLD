class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def create_memento(self):
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

# Create the objects
originator = Originator()
caretaker = Caretaker()

# Set the initial state
originator.set_state("State 1")

# Save the state
caretaker.add_memento(originator.create_memento())

# Change the state
originator.set_state("State 2")

# Save the state again
caretaker.add_memento(originator.create_memento())

# Restore the first saved state
originator.restore_from_memento(caretaker.get_memento(0))
print(originator.get_state())  # Output: State 1

# Restore the second saved state
originator.restore_from_memento(caretaker.get_memento(1))
print(originator.get_state())  # Output: State 2
