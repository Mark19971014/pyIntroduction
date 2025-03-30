class Student:
    def __init__(self, name):
        self.set_name(name)  # Use setter method

    def get_name(self):
        return self._name  # Using a private variable (_name)

    def set_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name  # Assign the validated name

student = Student("Alice")
print(student.get_name())  # Alice
student.set_name("Bob")  # Works fine
print(student.get_name())

class Student:
    def __init__(self, name):
        self.name = name  # Calls setter method (not direct access)

    @property
    def name(self):
        """Getter method"""
        return self._name

    @name.setter
    def name(self, name):
        """Setter method with validation"""
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name


student = Student("Alice")
print(student.name)  # Calls getter: "Alice"
student.name = "Bob"  # Calls setter: Updates name
