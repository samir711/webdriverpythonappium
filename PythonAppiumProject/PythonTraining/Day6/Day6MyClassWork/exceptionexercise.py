# Q1. Write down a program where we create a list of 5 numbers, write a step to access a value in the list, giving a wrong index
# #
# # print the exception by using e.args, and the class/type of exception encountered

num_list = [4, 5, 6, 45, 65]

try:
    print(num_list[9])

except Exception as e:
    print("Index of list is out of range", e.args)
    print(type(e))

else:
    print(num_list[9])
