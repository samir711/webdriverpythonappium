list1 = ['mountain', 'lakes', 2019, 1298]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0] : ", list1[0])
print("List2[1:", list2[1:5])

# Update item in the list
list1[3] = 100
print(list1)

# Delete item form the List

del list2[3]
print(list2)

list2.remove(6)
print(list2)

# Iterate through List

for i in list1:
    print(i)

for i in list2:
    print(i)

# List functions

print("Length of list 2 : : ", len(list2))
print("Maximum element of list 2 : ", max(list2))
print("Minimum element of list 2 : ", max(list2))
print("position of element in list : ", list1.index(2019))
list2.reverse()
print("reverse of list 2 : ", list2)
