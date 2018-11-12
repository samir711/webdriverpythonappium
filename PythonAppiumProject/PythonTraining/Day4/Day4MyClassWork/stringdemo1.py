# Q2. create a list of 5 string values, print the string which has max characters.


list_string = ["rose", "lilac", "lotus", "sunflower", "hyacinth"]

max_length = 0
op_str = ""

for flower in list_string:
    if max_length < len(flower):
        max_length = len(flower)
        op_str = flower

print(op_str)