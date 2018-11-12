#Ask end user to enter a number and find if the number is divisible by 2 or 3, or both

number =int(input("Enter the number: "))
print("If number is divisible by 2 or 3", (((number%2)==0)|((number%3)==0)))
print("If number is divisible by 2 and 3", (((number%2)==0) &((number%3)==0)))
