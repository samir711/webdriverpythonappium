def calculate_simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si


def calculate_amount(p, si):
    amount_value = p + si
    return amount_value


principle = int(input("Enter the principle: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter the duration: "))

# Calculate Interest

simple_interest = calculate_simple_interest(principle, rate , time)
print("Simple Interest is: ", simple_interest)

# Calculate amount

amount = calculate_amount(principle, simple_interest)
print("Amount to be paid", amount)