class Student:
    def __init__(self,name,gender,age,marks):
        self.name=name
        self.gender=gender
        self.age=age
        self.marks=marks
    
    def printPercent(self):
        percent=(self.marks/500)*100
        print("Name: ", self.name, ", Percent: " , percent)

stud1=Student("Paul","Male",30,390)
stud2=Student("Roma","Female",20,480)
stud3=Student("Fiona","Female",10,370)
stud1.printPercent()
stud2.printPercent()
stud3.printPercent()
marks=[stud1.marks,stud2.marks,stud3.marks]
marks.sort()
print(marks)