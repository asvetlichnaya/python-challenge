# Write a function that counts the number of vowels in a given word.
import re


def count_vowels_in_word(value: str):
    list_of_vowels = re.findall("[aeiouy]", value)
    return len(list_of_vowels)


input_string = input('Please input a word: ').strip()
print(count_vowels_in_word(input_string))
