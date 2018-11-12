flag = False
# Print Table for 2
m = 2
print(m)
for k in range(1,
               11):  # Another way to print information %d is string formatter, and end= '' is for prinitng in same line
    print("%d" % m, end=' '),
    print("*", end=' '),
    print("%d=" % k, end=' '),
    print(m * k)

# Find whether the number is Prime or not
for i in range(3, 11):
    for j in range(2, i):
        if (i % j == 0):
            flag = True
            break  # Exit the for loop
    if (flag):
        pass  # pass and move on to the next entry in the for loop do nothing.
    else:
        print(i)
        # If the number is Prime print the table
        for k in range(1, 11):
            print(i, "*", k, "=", i * k)
    flag = False
