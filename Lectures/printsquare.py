'''
Write a program that reads a positive integer n, and prints a n*n square, filled with '*' symbols.
'''

print("Please enter a positive integer: ")
n = int(input())

for i in range(n):
    print("*" * n)