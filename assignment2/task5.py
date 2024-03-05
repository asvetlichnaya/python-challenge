# Assignment2, Task5

# Rewrite the function from task 4, and now it should return a dictionary with the vowel as key and the number of the
# vowel in a word as value
import re


def count_vowels_in_word(value: str):
    list_of_vowels = re.findall("[aeiouy]", value)
    dict_of_vowels = {}
    for i in list_of_vowels:
        dict_of_vowels[i] = list_of_vowels.count(i)
    return dict_of_vowels


input_string = input('Please input a word: ').strip()
print(count_vowels_in_word(input_string))
