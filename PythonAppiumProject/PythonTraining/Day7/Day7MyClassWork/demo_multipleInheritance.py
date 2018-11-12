def add(*args) :

    int_answer = 0
    string_answer = ' '
    answer = True

    for x in args:
        if type(x) == int:
            int_answer = int_answer + x
        elif type(x) == str:
            string_answer = string_answer + x
            answer = False
        else:
            print("Input is not valid")

    if answer:
        print(int_answer)
    else:
        print(string_answer)


# add(2, 4)
add("Hello", " World")
# if type(phone_number_temp) == list