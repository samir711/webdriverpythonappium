fo = open("d:\\empfile.csv", "r")
for line in fo.readlines(): #.readline - returns first line read. readlines returns list of lines
    #print(line)
    data=line.split(",")
    print("Eid: ", data[0])
    print("EName: ", data[1])
    print("EDesignation: ", data[2])
    print("EGender: ", data[3])
fo.close()