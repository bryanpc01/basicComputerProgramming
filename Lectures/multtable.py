'''
Write a program that reads a positive integer and prints a n * n multiplication table
'''

n = int(input('Please enter a positive integer: '))

for row in range(1, n + 1):
    for i in range(1, n + 1):
        print(row * i, end="\t")
    print('')
