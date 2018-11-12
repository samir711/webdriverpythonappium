a=10
b=20

print("BREAK Example:")
for i in range(a,b):
    if(i==16):
        break
    else:
        print(i)
    
print("\nPASS Example:")
for j in range(a,b):
    if(j==14):
        pass
    else:
        print(j) 