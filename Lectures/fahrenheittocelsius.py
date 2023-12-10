'''
Write a program that reads from the user a temperature in Fahrenheit and converts it to Celsius.
'''


def main():
    fahr = float(input('Please enter temperature in Fahrenheit: '))
    cel = fahrenheit_to_celsius(fahr)
    print(fahr, "Fahrenheit is", cel, "Celsius")


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


main()

