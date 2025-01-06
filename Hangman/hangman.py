import  random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something fro the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words) # PYTHON
    word_letters=set(word) # letters in the word {'P', 'Y', 'T', 'H', 'O', 'N'}
    alphabet=set(string.ascii_uppercase)
    used_letters=set()# what the user has guessed

    lives=6
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        # what the current word is (ie W - R D)
        # word_list = []
        # for letter in word:"python" p
        #     if letter in used_letters:
        #         word_list.append(letter)
        #     else:
        #         word_list.append('-')
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter=input("Guess a letter: ").upper()
        if user_letter in alphabet-used_letters: # if used_letters = {'A', 'B'}, then alphabet - used_letters would be all uppercase letters except 'A' and 'B'
            used_letters.add(user_letter)
            if user_letter in word_letters: # njan 'p' guess cheyyumpol ath word_letter le undengil athine ivide ninn remove cheyyum
                word_letters.remove(user_letter)
            else:
                lives=lives - 1 # takes away a life if wrong
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that character.Please try again.')
        else:
            print('Invalid Characters.Please try again.')
    # gets here when len (word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You dies, sorry.The word was', word)
    else:
        print('You guessed the word', word, '!!')

hangman()