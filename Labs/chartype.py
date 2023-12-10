'''
Character Type Lab:

Description

Write a program that reads a character (string of  length 1) from the user, and classifies it to one of the following: lower case letter, upper case letter, digit, or non-alphanumeric character.

Sample output (4 different executions):

Enter a character: j
j is  a lower case  letter.

Enter a character: 7
7 is  a digit.

Enter a character: ^
^ is  a non-alphanumeric  character.

Enter a character: C
C is  an  upper case  letter.
'''

char = input('Enter a character: ')
if char.isupper():
    print(f'{char} is a uppercase letter.')
elif char.islower():
    print(f'{char} is a lowercase letter.')
elif char.isdigit():
    print(f'{char} is a digit.')
elif not char.isalnum():
    print(f'{char} is a non-alphanumeric character.')
