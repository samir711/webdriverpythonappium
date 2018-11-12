file_location = ".\..\..\data\\text_files\\write.txt"

# appending a File

file_write = open(file_location, "a+")  # append and read
file_write.write("I am good how are you!")
file_write.close()