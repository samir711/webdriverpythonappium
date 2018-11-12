#  create a list of 10 values, where you ask end user to provide the information. 
# 
# the information is the marks secured by 10 students for the subject maths. 
# 
# from the list provide the following information -
# 
# a. highest marks scored
# b. lowest marks scored
# c. average of the marks scored by first 5 students


number_list = []

for i in range(1, 10):
    num = int(input("Enter the number : "))
    number_list.append(num)

print("Highest score is ", max(number_list))
print("Lowest score is ", min(number_list))

scoreOfFirstFive = number_list[0:5]
score = 0
# for i in scoreOfFirstFive:
#     score += i
for i in range(0, len(scoreOfFirstFive) - 1):
    print(i)
    score += scoreOfFirstFive[i]

print(score/len(scoreOfFirstFive))
