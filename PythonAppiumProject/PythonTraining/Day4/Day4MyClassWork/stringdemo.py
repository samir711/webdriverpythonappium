# Ask  to  enter  a
# string, print
# its
# reverse.  # do not use the inbuilt reverse function if any


mystring = input("Please enter a string ")
newstr = ""
for i in range(len(mystring)-1, -1, -1):
    newstr = newstr + mystring[i]
print(newstr)


str = input("Enter data: ")
str1 = str[::-1]
print(str1)




