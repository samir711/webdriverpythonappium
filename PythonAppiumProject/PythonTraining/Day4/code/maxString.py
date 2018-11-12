listS=["rose", "liliac", "lotus", "sunflower", "hyacinth"]
max=0
opstr=""
#compare each string length as we iterate with max, if max is less than length make that length the new max and assign string.
#continue until end of list
for f in listS:
    if(max<len(f)):
        max=len(f)
        opstr=f

print(opstr)