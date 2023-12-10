'''
Even Numbers Lab:

Description

Write a program that reads a positive integer n, and prints the first n even numbers.

For example, one execution would look like this:

Please enter a positive integer: 3
2
4
6
'''

n = int(input('Please enter a positive integer: '))
for i in range(1, n + 1):
    print(2 * i)
