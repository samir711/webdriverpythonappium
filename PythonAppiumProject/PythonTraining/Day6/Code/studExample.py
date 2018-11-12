class Student:
    def __init__(self,name,age,percentage):
        self.name=name
        self.age=age
        self.percentage=percentage
    
    def printDetails(self):
        print("Name: ", self.name, ", Percent: " , self.percentage)

stud1=Student("Paul",10,45)
stud2=Student("Roma",12,76)
stud3=Student("Fiona",9,34)

stud1.printDetails()
stud2.printDetails()
stud3.printDetails()

if((stud1.age>stud2.age)&(stud1.age>stud3.age)):
    print(stud1.age)
elif((stud2.age>stud1.age)&(stud2.age>stud3.age)):
    print(stud2.age)
else:
    print(stud3.age)
    