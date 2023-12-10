'''
Write a program that reads front her user their full name and prints their first name, last name, and initials in
separate lines
'''

full_name = input('Enter your full name (seperated by a space): ')

index_of_space = full_name.find(' ')
first_name = full_name[:index_of_space]
last_name = full_name[index_of_space + 1:]
initials = first_name[0] + last_name[0]

print("First Name: " + first_name)
print("Last Name: " + last_name)
print("Initials: " + initials)