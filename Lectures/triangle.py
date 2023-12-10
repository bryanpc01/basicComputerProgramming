'''
Write a program that reads a positive integer n, and prints a n line right triangle, aligned to the left, filled with '*' symbols.
'''

n = int(input("Please enter a positive integer: "))

print("N-Lined Right Triangle Aligned to the Left")
for i in range(1, n + 1):
    print("*" * i)

print("N-Lined Right Triangle Aligned to the Right")
for i in range(1, n + 1):
    print(" " * (n-i) + "*" * i)
