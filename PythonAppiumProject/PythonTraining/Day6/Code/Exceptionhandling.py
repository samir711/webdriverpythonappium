
try:
    fh = open("c:/testfile", "w")
    fh.write("This is my test file for exception handling!!")
except Exception:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

#vs

#fh1 = open("c:/testfile", "w")
#fh1.write("This is my test file for exception handling!!")
#fh1.close()

print("outside code")