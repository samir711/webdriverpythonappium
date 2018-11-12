# . - any character
# * - 0 or more occ of prev expression
# + - 1 or more occ of prev expression
# ? - 0 or 1 occ of prev expression
# ^- start of an expression
# $ - end of the expression
# [a-z]- any alphabet
# [A-Z] - any caps alphabet
# [0-9]- any digit
# {m}- exactly m times
# {m,n} - min m times, max n times

# Q4. Create a regex to match any 10 digit mobile number which starts with 78
# 784-214-5478
# ^78[0-9]{8}$
# 321-09-4930, 893-23-9392, 931-76-2839....
# ^[0-9]{3}-[0-9]{2}-[0-9]{4}$
#
# \d - any digit
# \D - non digit
# \w- represents word
# \W - non word
# \s- space
# \S - no space

# 321-09-4930, 893-23-9392, 931-76-2839....

regular_expression = "^\d{3}-\d{2}-\d{4}$"

# Q6. '@', '.'
#
# alphanumeric@alpha.alpha
# start is always alphabet
#
# roma123@roma.com
# rhea@gmail.com
# tom21@biz.in

regular_expression = "^\w+\d*@\w+\\.\w+"