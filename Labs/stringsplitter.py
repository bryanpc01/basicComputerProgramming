'''
String Splitter Lab:

Description

Read from the user a string containing
odd number of characters. Your program should:

   a) Print the middle character.
   b) Print the string up to but not including the middle character (i.e., the first half of the string).
   c) Print the string from the middle character to the end (not including the middle character).

Sample output:

Enter an odd length string: Fortune favors the bold
Middle character: o
First half: Fortune fav
Second half: rs the bold
'''

string = input("Enter an odd length string: ")

middle_char = (len(string) // 2)
print("The middle character is:", string[middle_char])

first_half = string[:middle_char]
second_half = string[middle_char + 1:]

print("The first half is:", first_half)
print("The second half is:", second_half)
