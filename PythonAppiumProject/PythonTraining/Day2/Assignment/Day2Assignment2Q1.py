# Q1. Write down a program, which asks user to enter three values, print the smallest of them.

# Prompt user to enter the three numbers
number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter Third number : '))

# if , elif and else condition will be used to test the smallest number
smallest_num = 0

if (number1 < number2) and (number1 < number3):
    smallest_num = number1

elif (number2 < number1) and (number2 < number3):
        smallest_num = number2
else:
    smallest_num = number3

# Printing the smallest number

print("The smallest of the 3 numbers is : ", smallest_num)
