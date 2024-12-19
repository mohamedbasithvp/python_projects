import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, this is too low guess again")
        elif guess > random_number:
            print("Sorry, this is too high guess again")

    print(f"Yey, Congrats. you have guessed the number correctly")


guess(10)