import array as arr

intA = arr.array("I",[3,6,9,10,14,21,48])
print(intA)


#functions of array
intA.append(6)  #adds the value 6 at the end. 
print(intA)
print(intA.count(6))  #print the number of times 6 appear
print(intA.index(21))
print(intA.index(6)) # will return the position of the first 6 found

intA.insert(1,10)
print(intA)

intA.pop()  #removes last number
print(intA)

intA.remove(21) #removes first occ of 21
print(intA)

intA.reverse()
print(intA)