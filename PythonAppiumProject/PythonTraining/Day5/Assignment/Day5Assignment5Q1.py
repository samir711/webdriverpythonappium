# Q1. Write down a program which reads the contents of the file, and prints only the mobile number from it.
# contents - # "he vote, scores of protesters broke through 9028765112 barricades and staged a raucous sit-in protest
#  on the US Capitol steps. # # As protesters chanted "S 8371010382 # # n process has 3791038193 laid bare the
# partisan gridlock on 3801300482 Capitol Hill and the political polarization of America just a # #  and order and
# justice. And we really have become even more so than ever before the party of opportunity"

# content_file_location_project = loc = ".\..\..\data\\text_files\content.txt"
import re
from PythonTraining.Day5.Assignment.UserDefModule import remove_space_in_string


content_file_location_project_local = ".\\content.txt"  # Set File Location
phone_number_list = []        # List of Saving multiple phone number in content file

# Open content file (test file) in read only mode

file_read = open(content_file_location_project_local, "r")
for line in file_read.readlines():                         # read file lines
    phone_number = re.sub(r'\D', ' ', line)            # re to remove every thing from line except digit
    phone_number_temp = remove_space_in_string(phone_number) # remove spaces from the phone number
    if type(phone_number_temp) == list:   # if line is having multiple phone number split and add to phone_number_list
        for phone_list in phone_number_temp:
            phone_number_list.append(phone_list)
    elif phone_number_temp.strip().isdigit():        # Check if the phone number is digit then add to phone_number_list
        phone_number_list.append(phone_number_temp)
file_read.close()  # close the file

print(phone_number_list)  # print phone number
for phone_number_in_list in phone_number_list:
    print("The phone numbers in content file is : ", phone_number_in_list)
