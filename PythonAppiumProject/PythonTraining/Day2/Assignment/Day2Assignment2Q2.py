# Q2. Write down a program which take a number as input, and prints the factorial as output
# n!= n*n-1*n-2..*1
# 5!=5*4*3*2*1

# Prompt user to enter a number
num = int(input("Enter a number :  "))

# Initialize a variable for factorial

factorial = 1

# Check if the number is negative , positive or zero

if num < 0:
    print("Factorial does not exist for negtive number ")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):  # range (1, num) return 1 to num -1 to offset add 1 which will return 1 to num
        factorial *= 1
    print("The factorial of ", num , "is ", factorial)
