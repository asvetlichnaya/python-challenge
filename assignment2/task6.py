import re


def count_vowels_in_csv_file(text: str):
    split_string = re.split(r'\W+', text)

    count_of_vowels = {}
    x = {}
    for word in split_string:
        list_of_vowels = re.findall("[aeiouy]", word)
        x = {}
        for vowel in list_of_vowels:
            x[vowel] = list_of_vowels.count(vowel)
            count_of_vowels[word] = x
    return str(count_of_vowels)


with open('input_files/inputs.csv') as f:
    content = f.read()

with open('output_files/output.txt', 'w') as f:
    f.write(count_vowels_in_csv_file(content))
