#
# Q4. Based on the following table, find out the house tax to be paid by the individual.
#
# maritial status	housetax
# single		10%
# married		20%
# divorced		30%
# windower		5%

maritalStatus = input("Please enter marital status  : ")

if maritalStatus == "single":
    print("The applicable tax for Single is : 10 %")

elif maritalStatus == "married":
    print("The applicable tax for Married  is : 20 %")

elif maritalStatus == "divorced":
    print("The applicable tax for divorced  is : 30 %")

elif maritalStatus == "widower":
    print("The applicable tax for widower  is : 5 %")

else:
    print("Marital status is not valid")

