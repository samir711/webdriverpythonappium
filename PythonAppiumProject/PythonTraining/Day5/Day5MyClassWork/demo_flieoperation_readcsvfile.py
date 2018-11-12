file_location = ".\..\..\data\\csv_files\empfile.csv"

fo = open(file_location, "r")
for line in fo.readlines():
    # print(line, end="")
    data = line.split(",")
    print("Eid : ", data[0])
    print("EName: ", data[1])
    print("EDesignation : ", data[2])
    print("EGender: ", data[3])

fo.close()