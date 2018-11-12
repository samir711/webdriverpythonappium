import re


def remove_space_in_string(input_string):
    str_temp = input_string.strip()
    if str_temp.find(' ') != -1:
        str_temp = re.sub(r'\W\D\S', ',', str_temp)
        str_return = split_string(str_temp)
    else:
        str_return = str_temp
    return str_return


def split_string(input_string):
    temp_list = []
    if input_string.find(' ') != -1:
        temp = input_string.split(",")
        for i in temp:
         temp_list.append(i.strip())
    return temp_list