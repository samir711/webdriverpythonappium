str = input("enter a string:-")
newstr = ""
for i in range(len(str) - 1, -1, -1):
    newstr = newstr + str[i]

print(newstr)  # reverse string

# OR

str = input("Enter data: ")
str1 = str[::-1]
print(str1)
