class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):  # Overrides speak method
        return "Woof!"

dog = Dog()
print(dog.speak())  # Woof!


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading the + operator
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Calls __add__()
print(v3.x, v3.y)  # Output: 4, 6
