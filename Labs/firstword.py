'''
First Word Function Lab:

Description

Write a function that is given a phrase and returns the first word in that phrase. For example, given ‘the quick brown fox’, your function should return ‘the’.

Here is an example call to the function:

print(firstword(“the quick brown fox”)):
'''


def firstword(str):
    space_index = str.find(" ")
    return str[:space_index]

print(firstword("the quick brown fox"))