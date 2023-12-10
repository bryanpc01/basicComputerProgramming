'''
Coin Converter Lab:

Description

Write a program that asks the user to enter an amount of money in the format of dollars and remaining cents.
The program should calculate and print the minimum number of coins (quarters, dimes, nickels and pennies) that are equivalent to the given amount.

Hint: In order to find the minimum number of coins,
first find the maximum number of quarters that fit in the given amount of money,
then find the maximum number of dimes that fit in the remaining amount, and so on.
'''

print("Please enter an amount of and I will convert it to coins:/nExample: $3.10")
amount = float(input("$"))
print(f"The minimum number of coins that makes up ${amount:.2f} is:")

amount = int(amount * 100)

quarters = amount // 25
amount = amount - (quarters * 25)
print("Quarters:", quarters)

dimes = amount // 10
amount = amount - (dimes * 10)
print("Dimes:", dimes)

nickels = amount // 5
amount = amount - (nickels * 5)
print("Nickels:", nickels)

pennies = amount
print("Pennies:", pennies)
