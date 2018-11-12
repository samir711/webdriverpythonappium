#  Create a class called as student, which has the following properties - name, age, percentage.
# create three objects of the student class.
# create a method, display information which prints the name and percentage of student.


class Student:
    oldest_student = []
    oldestStudent = 0

    def __init__(self, name, age, percentage):
        self.name = name
        self.age = age
        self.percentage = percentage
        Student.oldest_student.append(age)

    def student_info(self):
        print("Name of Student is : ", self.name, ", and Age is : ", self.age, " Percentage Scored is : ", self.percentage)


student1 = Student("John", 16, 90)
student2 = Student("Alex", 17, 70)
student3 = Student("Mary", 44, 80)

student1.student_info()
student2.student_info()
student3.student_info()

print("\nThe oldest student is ", max(Student.oldest_student))
