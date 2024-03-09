import re


def count_vowels_in_csv_file(text: str):
    split_string = re.split(r'\W+', text)

    count_of_vowels = {}
    x = {}
    for j in split_string:
        list_of_vowels = re.findall("[aeiouy]", j)
        x = {}
        for i in list_of_vowels:
            x[i] = list_of_vowels.count(i)
            count_of_vowels[j] = x
    return str(count_of_vowels)


with open('input_files/inputs.csv') as f:
    content = f.read()

with open('output_files/output.txt', 'w') as f:
    f.write(count_vowels_in_csv_file(content))
