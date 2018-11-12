#Print numbers which are divisible by 7 given in a range

srange=int(input("Enter start range: "))
erange=int(input("Enter end range: "))

for i in range(srange,erange):
    if(i%7==0):
        print(i)



    