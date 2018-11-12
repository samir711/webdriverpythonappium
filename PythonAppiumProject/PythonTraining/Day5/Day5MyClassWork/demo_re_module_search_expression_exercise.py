import re

# Q3. Write down a program which expects a NRIC number.
#
# e.g. - S8832267C
#
# M9392309L
#
# B3820421K ...

line = input("Enter a pan NRIC number : ")
if re.search(r'^[A-Z]{1}\d{7}[A-Z]{1}$', line, re.M | re.I):
    print("The input String is a  NRIC number")
else:
    print("Junk value")
