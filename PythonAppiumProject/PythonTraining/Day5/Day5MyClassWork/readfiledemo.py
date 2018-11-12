# read file line by line

# fo = open("d:\\write.txt", "r")
# for line in fo.readlines(): #  readline - returns first line read. readlines returns list of lines
#     print(line)
# fo.close()


fo = open("d:\\write.txt", "r")
str = fo.read()
print("\n Read String is : ", str)
fo.close()