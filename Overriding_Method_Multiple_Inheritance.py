class Base1:
    def __init__(self):
        print('Base1 class')
    
    def disp(self):
        print('display base1 method')
    
class Base2:

    def __init__(self):
        print('Base2 class')
    
    def disp(self):
        print('display base2 method')
        
class Derived(Base1, Base2):
     pass
 
 
'''
This code will will be called on the main module only, when this module is imported
this will not be called
'''
if(__name__ == '__main__'): 
    d = Derived()
    d.disp()

    
    