'''
Write a program that reads from the user 3 words and prints the word that comes first in alphabetical order
'''

print("Please enter three words:")
word1 = input("First word: ")
word2 = input("Second word: ")
word3 = input("Third word: ")

if (word1 <= word2 and word1 <= word3):
    print(word1)
elif (word2 <= word1 and word2 <= word3):
    print(word2)
else:
    print(word3)