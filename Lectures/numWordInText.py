'''
Write a program that reads a line of text from the user and prints the number of words in the that text
'''

user_input = input("Enter a line of text: ")

num_of_spaces = 0
for char in user_input:
    if char == " ":
        num_of_spaces += 1

print(f"You entered {num_of_spaces + 1} words.")
