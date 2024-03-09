# Assignment2, Task4

# Write a function that counts the number of vowels in a given word.
import re


def count_vowels_in_word_ver1(sentence: str):
    list_of_vowels = re.findall("[aeiouy]", sentence)
    return len(list_of_vowels)


def count_vowels_in_word_ver2(sentence: str):
    count = 0
    for i in sentence:
        if i in ['a', 'e', 'i', 'o', 'u', 'y']:
            count = count + 1
    return count


input_string = input('Please input a word: ').strip()
print(count_vowels_in_word_ver1(input_string))
print(count_vowels_in_word_ver2(input_string))
