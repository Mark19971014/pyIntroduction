import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def __init__(self, owner):
        self.owner = owner  # Instance attribute

    # Instance method
    def sort(self):
        print(f"{self.owner} is in {random.choice(self.houses)}")  # Uses self

    # Class method
    @classmethod
    def add_house(cls, house):
        cls.houses.append(house)  # Modifies class attribute

    # Static method
    @staticmethod
    def random_house():
        return random.choice(["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"])



hat1 = Hat("Harry")

hat1.sort()  #Uses instance attribute (requires an object)

Hat.add_house("Ilvermorny")  # Modifies class attribute

print(Hat.random_house())  # No instance required, works like a utility function
