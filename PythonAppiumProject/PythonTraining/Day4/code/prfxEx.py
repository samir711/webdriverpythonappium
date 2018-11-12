name = input("enter name with prefix Mr for male, Ms for female, no prefix for neutral: ")
if(name.startswith("Mr.")):
    print("male")
elif(name.startswith("Ms.")):
    print("female")
else: 
    print("neutral")
