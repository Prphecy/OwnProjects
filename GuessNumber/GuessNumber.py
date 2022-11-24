import random
from re import L

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) 
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
    print(f'Congrats. You have guessed the number {random_number} correctly!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': 
        if low != high:
            guess = random.randint(low, high)
        else :
            guess = low #could be also be high b/c low=high    
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback  == 'h':
            high = guess -1 
        if feedback == 'l':
            low = guess + 1
    print(f'Yep, the computer guess your number, {guess}, correctly')

computer_guess(69)       