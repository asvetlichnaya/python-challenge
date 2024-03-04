# Assignment2, task3

# Write a function to check duplicate letters in words. It must accept strings i.e. a sentence.
# The function should return True if any of the words has duplicate letters else return False.
import re


def if_duplicate_letters_exists(value: str, flag=False):
    split_string = re.split(r'\W+', value)
    for word in split_string:
        for letter in word:
            if letter in word[word.index(letter) + 1:len(word):1]:
                flag = True
                break
    return flag


input_string = input('Please input a string: ').strip()
print(if_duplicate_letters_exists(input_string))
