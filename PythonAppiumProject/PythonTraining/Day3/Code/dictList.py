employeeDict={'E001':['Tom',43,'CEO'],'E002':['Roma',44,'VPHR']}

for i in employeeDict.keys():
    print("ID:", i)
    print("Name:", employeeDict[i][0])
    print("Age: ", employeeDict[i][1])
    print("Designation: ", employeeDict[i][2])
    print("\n")