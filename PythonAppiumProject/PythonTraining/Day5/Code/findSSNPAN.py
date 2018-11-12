#Ask user to enter a string find whether it is ssn or pan card
import re

line = input("Enter a pan card or ssn: ")

#Search for PanCard
if(re.search( r'^[A-Z]{5}\d{4}[A-Z]{1}$', line, re.M|re.I)):
    print("The input String is a Pancard")
elif(re.search( r'^\d{3}-\d{2}-\d{4}$', line, re.M|re.I)):
    print("The input String is a SSN")
else:
    print("Junk value")
   

