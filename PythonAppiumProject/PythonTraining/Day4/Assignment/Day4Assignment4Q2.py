# Q2. Write down a program which asks user to enter a string, and prints if the string is palindrome or not
# same as its mirror image
# test data - malayalam


def is_string_palindrome(test_string):
    """Test string is palindrome
        Author : Samir
        input : test string
       output : print the input string is palindrome or not .
       """
    if test_string == test_string[::-1]:
        print("The string is a palindrome")
    else:
        print("The string isn't a palindrome")


input_string = input("Enter a string : ")
is_string_palindrome(input_string)
