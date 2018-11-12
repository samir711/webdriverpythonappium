# Q2. Write down a program where we take input from the end user, and
#     find out if the number  is divisible by 5 but not 7 

number = int(input("Enter the number : ")) 

print("Is number is divisible by 5 but not 7", (((number% 5 )==0) & ((number%7)!=0)))

