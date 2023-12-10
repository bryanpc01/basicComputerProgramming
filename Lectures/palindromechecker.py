'''
Write a program to check if a string is a palindrome.
'''


def main():
    user_string = input('Enter a string: ')
    str_for_checking = prepare_str_for_palindrome_checking(user_string)
    if (is_palindrome(str_for_checking)):
        print("Your sentence is a palindrome.")
    else:
        print("Your sentence is not a palindrome.")


def is_palindrome(s):
    return True if s == reverse_string(s) else False


def prepare_str_for_palindrome_checking(s):
    return keep_only_letters(s).lower()


def keep_only_letters(s):
    res_str = ''
    for char in s:
        if char.isalpha():
            res_str += char
    return res_str


def reverse_string(s):
    tmp_str = ''
    for char in s:
        tmp_str = char + tmp_str
    return tmp_str


main()
