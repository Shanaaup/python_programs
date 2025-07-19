import random

class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first, second
d1=Dice()
print(d1.roll())