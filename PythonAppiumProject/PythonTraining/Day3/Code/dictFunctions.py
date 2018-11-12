
my_dict = {'name':'Joanna', 'age': 29}

#Fetch Data

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# update value
my_dict['age'] = 27
print(my_dict)

# add item
my_dict['address'] = 'London'  
my_dict['designation'] = 'CEO'  
print(my_dict)


# remove a particular item
print(my_dict.pop('age'))  

# remove an arbitrary item
print(my_dict.popitem())

# delete a particular item
del my_dict['name']  
print(my_dict)

# remove all items
my_dict.clear()
# Output: {}
print(my_dict)

#update dict
my_dict['name'] = 'Roma'  
my_dict['age'] = 32
my_dict['address'] = 'new york'
my_dict['designation'] = 'CTO'  
print(my_dict)

#membership test
print('name' in my_dict)
print('sal' not in my_dict)

# delete the dictionary itself
del my_dict
#print(my_dict)

