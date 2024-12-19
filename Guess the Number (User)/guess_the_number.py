import random

def computer_vision(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
        if low != high:
            guess=random.randint(low, high)
        else:
            guess=low
        feedback=input(f'is {guess} too high (H), too low (L), or correct (C)')

        if feedback == 'h':
            high=guess-1
        elif feedback == 'l':
            low=guess+1
    print(f'Yey! The Computer your number, {guess}, correctly')

computer_vision(10)