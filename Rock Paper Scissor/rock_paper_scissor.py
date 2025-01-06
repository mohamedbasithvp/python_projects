import random

def play():
    user=input("'r' for rock, 'p' for paper, 's' for scissor" )
    computer=random.choice(['r', 'p', 's'])
    print(computer)
    if is_win(user, computer):
        return 'You Win!'
    if is_die(user, computer):
        return 'Die'
    return' You Lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def is_die(player,opponent):
    if (player == 'r' and opponent == 'r') or (player == 's' and opponent == 's') or (player == 'p' and opponent == 'p'):
        return True

print(play())