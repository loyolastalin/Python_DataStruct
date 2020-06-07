# defining a simple class
class Point:
    def __init__(self, x, y): # constructor
        self.x = x
        self.y = y
    def move(self):
        print('move')


x1 = Point(10, 20);
print(x1.x)
x1.move();

# defining a simple class
class Person:
    def __init__(self, firstName):
        self.name = firstName
    def talk(self):
        print('talkin the user name {}'.format(self.name))

stalin = Person('stalin')
print(stalin.name)
stalin.talk();