from interface import implements
from Dy7.car import ICar

class BMW(implements(ICar)):
    def mileage(self):
        return "10"
    
    def color(self):
        return "black"
    
   
car1 = BMW()
print(car1.mileage())
print(car1.color())

