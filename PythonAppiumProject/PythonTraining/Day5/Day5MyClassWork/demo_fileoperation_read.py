loc = ".\..\..\data\\text_files\write.txt"

# readlines - read file line by line, return line by line
file_read = open(loc, "r")
for line in file_read.readlines():  # readlines - returns first line  and read line by line
    print(line, end='')
file_read.close()

# read  file and returns list of lines
file_read = open(loc, "r")
file_content = file_read.read()
print("\n Read String is : ", file_content)
file_read.close()