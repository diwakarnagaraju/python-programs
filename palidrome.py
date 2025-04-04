# write a Python program to check if a given string is a palindrome

word = input("Enter a word you wish: ")

word = word.lower()

if word == word[::-1]:
    print(f"you Entered word {word} is palindorme")
else:
    print(f"you enterd word {word} is not a palindorme")