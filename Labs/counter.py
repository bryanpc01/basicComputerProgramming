'''
Coin Counter Lab:

Description

Write a program that asks the user to enter a number of quarters, dimes, nickels and pennies and then outputs the monetary value of the coins in the format of dollars and remaining cents. Your program should interact with the user exactly as it shows in the following example:


Please enter the number of coins:
# of quarters: 20
# of dimes: 4
# of nickels: 13
# of pennies: 17
The total is 6 dollars and 22 cents
'''

print("Please enter the number of quarters, dimes, nickels and pennies:")
num_quarters = int(input("Quarters: "))
num_dimes = int(input("Dimes: "))
num_nickels = int(input("Nickels: "))
num_pennies = int(input("Pennies: "))

total = num_quarters * 25 + num_dimes * 10 + num_nickels * 5 + num_pennies * 1

print("The total is", total // 100, "dollars and", total % 100, "cents.")
