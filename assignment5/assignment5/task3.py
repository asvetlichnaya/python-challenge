import random


def play_game(user_c, computer_c):
    if user_c == computer_c:
        print('It is a draw')
        return 0
    elif user_c == 'paper' and computer_c == 'scissors':
        print('Computer won!')
        return -1
    elif user_c == 'paper' and computer_c == 'rock':
        print('You won!')
        return 1
    elif user_c == 'scissors' and computer_c == 'paper':
        print('You won!')
        return 1
    elif user_c == 'scissors' and computer_c == 'rock':
        print('Computer won!')
        return -1
    elif user_c == 'rock' and computer_c == 'paper':
        print('Computer won!')
        return -1
    elif user_c == 'rock' and computer_c == 'scissors':
        print('You won!')
        return 1


computer_win = 0
user_win = 0

choices = ['paper', 'scissors', 'rock']
while computer_win < 3 and user_win < 3:
    user_choice = input('Please type "paper, scissors or rock": ')
    computer_choice = random.choice(choices)
    print('Computer choice is ', computer_choice)

    result = play_game(user_choice, computer_choice)
    if result == 1:
        user_win = user_win + 1
    elif result == -1:
        computer_win = computer_win + 1

    print('Computer points are ', computer_win, 'User points are ', user_win)