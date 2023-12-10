'''
Fibonacci Lab:

Description

Fibonacci number is a series of numbers in which each number is the sum of the two preceding numbers. The first two numbers in the series are the number 1. Write a program to print first n Fibonacci Numbers.

For example, one execution would look like this:

Please enter a positive integer greater than 1: 4
1
1
2
3
'''

n = int(input("Please enter a positive integer greater than 1: "))
num1 = 1
num2 = 1

print(num1, num2, end=" ")
for _ in range(n - 2):
    new_num = num1 + num2
    print(new_num, end=" ")
    num1 = num2
    num2 = new_num
