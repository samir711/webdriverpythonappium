#
# Q5. Write down a program which prints the multiplication table of all the prime numbers between 1-20
#
# 2*1=2
# 2*2=4
# 2*3=6..
#
# 2*10=20
#
# 3..
#
# 5..
#
# 7..
# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.

lower_number = 1
upper_number = 20

for p_num in range(lower_number, upper_number + 1):
    if p_num > 1:                                               # Check if the number is greater than 1
        for i in range(2, p_num):
            if (p_num % i) == 0:                             # Check modulus of prime number
                break
        else:
            print("prime number is ", p_num)
            print("*********** Print Table Of - ", p_num, "***************")
            for i in range(1, 11):
                print(p_num, ' X ', i, '=', p_num * i)
            print("*****************************************************")