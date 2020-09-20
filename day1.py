# Write a Python program to test whether a passed letter is a vowel or not.

def is_vowel(input):
    list_vowels = 'aeiouAEIOU'
    return input in list_vowels

print(is_vowel('D'))
print(is_vowel('f'))
print(is_vowel('a'))
print(is_vowel('E'))
