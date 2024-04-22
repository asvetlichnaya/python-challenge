import random


with open('tips.txt', 'r') as file:
    lines = file.read().split('\n')

    print(random.choice(lines))
