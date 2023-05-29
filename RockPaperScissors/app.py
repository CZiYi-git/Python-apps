import random
from time import sleep

print('Round start!')

# range(start,stop,step)
for i in range(3,0,1):
    print(f'{str(i)}....')
    sleep(1)

# Ask player for choice
player_choice = input('Choose your option!')

# Ai makes a choice
ai_choice = random.choice(['rock','paper','scissors'])
print(f'AI chose {ai_choice}')

# Check for winner function
def checkwinner(player,ai):

    lose = 'You Lose!'
    tie = 'Its a Tie!'
    win = 'You Win! WOOOO'

    # Rock
    if player == 'rock' and ai == 'paper':
        return lose
    if player == 'rock' and ai == 'rock':
        return tie
    if player == 'rock' and ai == 'scissors':
        return win

    # Paper
    if player == 'paper' and ai == 'scissors':
        return lose
    if player == 'paper' and ai == 'paper':
        return tie
    if player == 'paper' and ai == 'rock':
        return win

    # Scissors
    if player == 'scissors' and ai == 'rock':
        return lose
    if player == 'scissors' and ai == 'scissors':
        return tie
    if player == 'scissors' and ai == 'paper':
        return win
    
    return lose

# Use checkwinner function
print(checkwinner(player_choice,ai_choice))
