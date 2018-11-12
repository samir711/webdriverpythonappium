listP = [1, 2, 3, 4, 5]

print(listP)

# Append a list
listP.append(7)
print(listP)

# Copy the list to new list
listQ = listP.copy()
print(" listQ is : ", listQ)

# Extend the list - concatenate two list together
listP.extend(listQ)
print(listP)

# Insert in the list at position or index

listP.insert(3, "hello")
print(listP)

# Remove item from the list

listP.pop(3)  # work on index, this will remove item at index 3
print(listP)

listP.remove(4)  # work on actual item of list, this will remove item 4 from the list
print(listP)

# Sort list
listP.sort()
print(listP)

# Count the occurrence of item in a list
print(listP.count(3))

# Delete specific range ot item in the list

del listP[2:4]
print(listP)
