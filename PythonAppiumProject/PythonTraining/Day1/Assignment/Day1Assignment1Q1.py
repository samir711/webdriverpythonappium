# Q1. Write down a program where we ask user to enter measurement for a sqaure, a rectangle and a circle. based on the information,
# we print the area and the Perimeter calculated. 
from builtins import int

# Calculate the Area and Perimeter of Square

lengthOfSquare = float(input("Enter the length of Square : "))
print("The area of Square is " , lengthOfSquare * lengthOfSquare)
print("The Perimeter of sqaure is " , 4 * lengthOfSquare)


# Calculate the Area and Perimeter of rectangle

lenghtOfRectangle = float(input("Enter the length of Rectangle : "))
widthOfRectange = float(input("Enter the widht of Rectangle : "))

print("The area of Rectangle  is " , lenghtOfRectangle * widthOfRectange)
print("The Perimeter of Rectangle  is " , 2 * (lenghtOfRectangle * widthOfRectange))

# Calculate the Area and Perimeter of Circle

PI = 3.14
radiusOfCircle = float(input("Enter radius of Circle : "))

print("The area of Circle  is " ,  PI * radiusOfCircle * radiusOfCircle)
print("The Perimeter of Rectangle  is " , 2 * PI * radiusOfCircle)


