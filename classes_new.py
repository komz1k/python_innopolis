"""мой первый класс"""

import random

class Human:
    genom_count = 46

    def __init__(self, name: str, age: int, descriptions: str):
        self.name = name
        self.age = age
        self.descriptions = descriptions

    def show_descriptions(self):
        print(f"{self.name} {self.descriptions}, {self.age} years old")

    @classmethod
    def get_genom_count(cls):
        return cls.genom_count

    @classmethod
    def set_genom_count(cls, count: int):
        cls.genom_count = count
    @staticmethod
    def choice_name():
        return random.choice(("Даша", "Маша", "Света", "Юля"))



human = Human("Даша", 16, "sports")

print(human.genom_count)
human.show_descriptions()
human.set_genom_count(4)
print(human.genom_count)
#print(human.__dict__)
#print(Human.__dict__)
print(human.choice_name())
