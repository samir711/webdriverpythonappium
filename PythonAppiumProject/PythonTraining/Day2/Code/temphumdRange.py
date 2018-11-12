temp=int(input("Enter the temp:"))
humid=int(input("Enter the humidity:"))

if((temp in range(0,21)) & (humid in range(0,21))):
    print("cold")