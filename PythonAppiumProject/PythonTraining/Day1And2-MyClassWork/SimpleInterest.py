principal = int(input("Please enter the principal amount : "))
rate = float(input("Please enter the rate of interest : "))
time = int(input("Please enter the tenure : "))

simpleinterest = (principal * rate * time) / 100

print("The simple inerest is {0}".format(simpleinterest))