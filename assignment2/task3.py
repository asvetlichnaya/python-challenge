# Assignment2, Task3

# Write a function to check duplicate letters in words. It must accept strings i.e. a sentence.
# The function should return True if any of the words has duplicate letters else return False.
import re


def if_duplicate_letters_exists_ver1(sentence: str):
    split_string = re.split(r'\W+', sentence)
    for word in split_string:
        for letter in word:
            if letter in word[word.index(letter) + 1:len(word):1]:
                return True
    return False


def if_duplicate_letters_exists_ver2(sentence: str):
    split_string = re.split(r'\W+', sentence)
    for word in split_string:
        if len(set(list(word))) != len(word):
            return True
    return False


input_string = input('Please input a string: ').strip()
print(if_duplicate_letters_exists_ver1(input_string))
print(if_duplicate_letters_exists_ver2(input_string))
