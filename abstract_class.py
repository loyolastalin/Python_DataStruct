from abc import ABC, abstractmethod

class IEmployee(ABC):
    
    @abstractmethod
    def calculate_Salary(self):
        pass
'''
v = IEmployee()
Abstact calss can't be instanciate 
By doing that you will get the bellow error
    Traceback (most recent call last):
      File "/home/main.py", line 9, in <module>
        v = IEmployee()
    TypeError: Can't instantiate abstract class IEmployee with abstract methods calculate_Salary
'''

class SalariedEmployee(IEmployee):
    def calculate_Salary(self):
        print('calculate_Salary for SalariedEmployee')

sa = SalariedEmployee()
sa.calculate_Salary()