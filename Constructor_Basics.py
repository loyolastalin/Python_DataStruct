class Base:
    def __init__(self, a):
        print('Base class', a)

class Derived(Base):

    def __init__(self, b):
        print('Derived class')
        super().__init__(b+3)
        
   
        
d = Derived(5)