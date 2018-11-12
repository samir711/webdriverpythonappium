currency= float(input("Enter the dollar amount : "))

currency = currency * 100
dollar = int(currency / 100)
print("Dollar -" , dollar)

ra = currency % 100

quarters = int(ra / 25)
print("Quater - ", quarters)
ra = int(ra % 25)

dimes = int(ra / 10)
print("dime - " , dimes)

ra = int(ra % 10)

nickle = int(ra / 5)
print("nickle - ", nickle)

ra = int(ra %5)

cents  = int(ra / 1)

print("cents - ", cents)
    
((num % 2 == 0) | (num % 3 == 0))
    

