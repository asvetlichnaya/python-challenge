# Assignment2, Task2

# Write a word counter: as input program accepts a txt file, then reads the content from the file and as
# output prints the number of words in that txt file.
# You need to create this txt file first and fill it with some sentences.
import re

with open('files/input_file.txt') as f:
    content = f.read()
    print(content)
    print('There are ', len(re.split(r'\W+', content)), ' words')
