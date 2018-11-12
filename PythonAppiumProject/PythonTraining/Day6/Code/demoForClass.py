class Employee:
    empCount = 0  #class variable
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
    
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
#call the method
emp1.displayEmployee()
emp2.displayEmployee()
print(emp1.name)
print("Total Employees: ",Employee.empCount)
