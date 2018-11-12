import re

phone = "2004-959-559 # This is Phone Number"

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print("Phone Num : ", num)


print(re.split("\W+", "This... is a test"))  # will split the string on a non word char.