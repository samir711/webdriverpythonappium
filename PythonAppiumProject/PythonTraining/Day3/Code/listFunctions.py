listP=[1,2,3,4,5]
listP.append(7)
print(listP)

listQ=listP.copy()
print(listQ)

listP.extend(listQ)
print(listP)

listP.insert(3,"hello")
print(listP)

listP.pop(3) #works on index
print(listP)

listP.remove(4) #actual data point
print(listP)

listP.sort()
print(listP)

print(listP.count(3))

del listP[2:4]
print(listP)