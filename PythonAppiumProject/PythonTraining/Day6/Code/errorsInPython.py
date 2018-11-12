
#syntax error
num=int(input("Enter a number: "))
prnt(num) #correction print

#Run Time Error
marks = [90,100,32]
print(marks[3]) #IndexError: list index out of range

#logical errors
a=10
b=20
if(a<b): #wrong usage of comparison operator
    print("a is greater")
    