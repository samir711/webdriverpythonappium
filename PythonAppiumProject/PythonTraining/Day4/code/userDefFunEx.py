def calculateSimpleInterest(p, r, t):
    si = (p * r * t) / 100
    return si


def calculateAmount(p, si):
    amnt = p + si
    return amnt


principle = int(input("Enter the principle: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter the duration: "))

# calculate amount
simpleInt = calculateSimpleInterest(principle, rate, time)
print("Simple Interest is: ", simpleInt)

# calculate Amount
amount = calculateAmount(principle, simpleInt)
print("Amount to be paid", amount)
