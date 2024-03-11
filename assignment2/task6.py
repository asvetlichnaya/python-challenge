import re


def count_vowels_in_csv_file(text: str):
    split_string = re.split(r'\W+', text.lower().strip())
    n_vowels_in_str = {}
    for word in split_string:
        count_of_vowels = {}
        for letter in word:
            if letter in {'a', 'e', 'i', 'o', 'u', 'y'}:
                x = count_of_vowels.get(letter)
                if x is None:
                    count_of_vowels[letter] = 1
                else:
                    count_of_vowels[letter] = x + 1
        n_vowels_in_str[word] = count_of_vowels
    return str(n_vowels_in_str)


with open('input_files/inputs.csv') as file:
    content = file.read()
    print(count_vowels_in_csv_file(content))

with open('output_files/output.txt', 'w') as file:
    file.write(count_vowels_in_csv_file(content))