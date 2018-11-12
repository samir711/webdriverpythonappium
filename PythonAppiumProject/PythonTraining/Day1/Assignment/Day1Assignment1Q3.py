# Q3. Ask user to enter the following information -
# 
# P = the principal investment amount (the initial deposit or loan amount)
# r = the annual interest rate (decimal)
# n = the number of times that interest is compounded per year
# t = the number of years the money is invested or borrowed for

principal = int(input("Enter the principal investment amount (the initial deposit or loan amount : "))
inerestRate = float(input("Enter the annual interest rate (decimal): "))
n = int(input("Enter the number of times that interest is compounded per year : "))
numberOfYear = int(input("Enter the number of years the money is invested or borrowed for : "))

compoundInterest = principal * (((1 + ((inerestRate / 100.0)/n)) ** (n* numberOfYear)))

print("The compound interest after", numberOfYear, "year is ", compoundInterest)