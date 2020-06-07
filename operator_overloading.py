class Employee:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __add__(self, others): # Operator overloading + 
        newname = self.name + others.name
        newAge = self.age + others.age
        return Employee(newname, newAge)
    def __str__(self): # Operator overloading for tostring
       
        return '{} {}'.format(self.name, self.age)

emp1 = Employee('Stalin', 39)
emp2 = Employee('Soosai', 39)

combined = emp1 + emp2
print(combined)
print('name {} , age {}'.format(combined.name, combied.age))