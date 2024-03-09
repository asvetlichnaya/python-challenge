# Assignment2, Task5

# Rewrite the function from task 4, and now it should return a dictionary with the vowel as key and the number of the
# vowel in a word as value
import re


def count_vowels_in_word_ver1(sentence: str):
    list_of_vowels = re.findall("[aeiouy]", sentence)
    count_of_vowels = {}
    for i in list_of_vowels:
        count_of_vowels[i] = list_of_vowels.count(i)
    return count_of_vowels


def count_vowels_in_word_ver2(sentence: str):
    count_of_vowels = {}
    for letter in sentence:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            x = count_of_vowels.get(letter)
            if x is None:
                count_of_vowels[letter] = 1
            else:
                count_of_vowels[letter] = x + 1
    return count_of_vowels


input_string = input('Please input a word: ').strip()
print(count_vowels_in_word_ver1(input_string))
print(count_vowels_in_word_ver2(input_string))
