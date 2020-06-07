# inheritance
class Base:
    def walk(self):
        print('walk')

class Dog(Base):
    def Park(self):
        print('Park')

class  Cat(Base):
    pass

dog1 = Dog()
dog1.walk()
dog1.Park()