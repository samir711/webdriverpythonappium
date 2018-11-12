class Animalia:
    def __init__(self, age, gender):
        self.age=age
        self.gender=gender
        
    def movement(self):
        print("limbs are used for movement ")
        
    def breath(self):
        print("they can breath")
            
    def diet(self):
        print("they have diet")
        
class LandAnimal(Animalia):
    
    def __init__(self,age,gender):
        self.age=age
        self.gender=gender
       
    def canRun(self):
        print("can run")
        
    def breath(self): #Method Overriding
        print("through lungs")
        
    def movement(self,limbs):
        print("limbs used for movement: ", limbs)


print("animal class:")
ani=Animalia(3,"female") #Parent Class
ani.breath() #Parent Class

print("child class:")
childani=LandAnimal(2,"male") #Child Class
childani.canRun() #Child Class Function
childani.diet() #Parent Class function
childani.breath()  #overridden func
childani.movement(4)  #overloaded func



    
    
        
        
    
        
        
        