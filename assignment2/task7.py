import json


def translate_to_morse(text: str):
    with open('input_files/morse_code.json') as file:
        morse_code = json.load(file)
    text = text.lower().strip()
    morse_string = ''

    for letter in text:
        if letter in morse_code.keys():
            morse_string = morse_string + morse_code[letter]
        else:
            morse_string = morse_string + letter
    return morse_string


input_string = input('Please input a string : ')
print(translate_to_morse(input_string))
