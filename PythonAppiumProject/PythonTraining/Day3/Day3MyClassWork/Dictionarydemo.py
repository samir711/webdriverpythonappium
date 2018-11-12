dictMonths = {'1': 'January', '2': 'February', '3': 'March', '4': 'April'}
# print one element
print("dictMonths['1']: ", dictMonths['1'])
# iterate through hash
for i in dictMonths.keys():
    print(i, dictMonths[i])

# Dictionary functions

print(dictMonths.items())  # print key value pair
print(dictMonths.keys())  # print only keys
print(dictMonths.values())  # print only values
