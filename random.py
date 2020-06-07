import random

class Dice:
    def roll(self):
        return (random.randint(1, 10), random.randint(10, 20))


dice = Dice()
x, y = dice.roll()
print(x,y)

print(random.random()) # range between  0 -1
print(random.choice([1,2,4]))