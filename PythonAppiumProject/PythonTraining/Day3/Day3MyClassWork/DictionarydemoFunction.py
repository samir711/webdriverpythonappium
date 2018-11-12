my_dict = {'name' : 'Joanna', 'age': 29}

# Getting the value of key using the key
print(my_dict['name'])

# Getting the value of key using the get function
print(my_dict.get('age'))

# Updating value of Key

my_dict['age'] = 45
print(my_dict)

# Adding Key value pair to dictionary

my_dict['address'] = "London"
my_dict['designation'] = 'CEO'

print(my_dict)

# Removing the particular key from the dictionary
my_dict.pop('age')
print("New dictionary after removing the Key age is : ", my_dict)


# Remove last item for the dictionary

my_dict.popitem()
print("New dictionary after removing the last  Key is : ", my_dict)

# Removing the a particular key from the dictionary

del my_dict['name']
print(my_dict)

# Remove all the key values for the dictionary

my_dict.clear()
print(my_dict)

# Update dictionary

my_dict['name'] = 'Roma'
my_dict['age'] = 32
my_dict['address'] = 'new york'
my_dict['designation'] = 'CTO'
print(my_dict)

# membership test - check whether key exits in dictionary
print('name' in my_dict)
print('sal' not in my_dict)

# Delete complete dictionary
del my_dict
#print(my_dict)


