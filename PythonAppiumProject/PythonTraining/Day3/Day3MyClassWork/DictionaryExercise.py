# Create a dictionary where the following data is available - 
# 
# Employee id:[Employee name, Employee Age, Employee designation] 
# 
# E001: [Tom,43,CEO]
# E002:[Roma, 34, VPHR]
# E003:[Frieda, 56, CTO]
# E004:[Harry, 52, CFO] 
# 
# iterate through the dictionary and print the information as follows for each employee record
# 
# ID- E001
# Name- Tom
# Age- 43
# Designation- CEO

employeeDictionary = {'E001': ['Tom', 43, 'CEO'], 'E002': ['Roma', 34, 'VPHR'], ' E003': ['Frieda', 56, 'CTO'], 'E004': ['Harry', 52, 'CFO'] }

for i in employeeDictionary.keys():
    print("ID : " , i)
    print("Name : ", employeeDictionary[i][0])
    print("Age : ", employeeDictionary[i][1])
    print("Designation", employeeDictionary[i][2])
    print('\n')
    # emplist = employeeDictionary[i]
    # print(emplist[0])
    # print(emplist[1])
    # print(emplist[2])

    # for j in emplist:
    #     print(j, end=' ')