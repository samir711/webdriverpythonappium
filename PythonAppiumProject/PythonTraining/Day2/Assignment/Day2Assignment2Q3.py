# Q3.Write down a program which prints the fibonacci series uptil 100
#
# 0 1 1 2 3 5 8 13 21....

# First two number of fibonacci series
fbn1 = 0
fbn2 = 1

number = 100
count = 0

print("fibonacci sequence up to : ", number, ": ")
while count < number:
    print(fbn1, end=' , ')
    fb_nth = fbn1 + fbn2
    # update values
    fbn1 = fbn2
    fbn2 = fb_nth
    count += 1
