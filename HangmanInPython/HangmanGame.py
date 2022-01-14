import random
from words import words
#the name of library is words and the name of variable from which we are importing is also 
from hangman_visual import lives_visual_dict
#the namae of library is hangman_visual and we are importing the variable lives_visual_dect for building the hangman 
import string


def get_valid_word(words):
    word = random.choice(words)
    # randomly chooses something from the list
    while '-' in word or ' ' in word:
    #keeps chosing till it encounters a - or gap 
        word = random.choice(words)
    return word.upper()

    #we convert the word into all upper 


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    # letters in the word are sent into a set since its immutable and cannot be changed 
    alphabet = set(string.ascii_uppercase)
    # this is the set of all alphabets of all uppercase 
    used_letters = set() 
    # what the user has guessed

    print("\n\n DIFFICULTY LEVELS \n")
    print("1. EASY and no. of lives = 10\n")
    print("2. TOUGHER and the no. of lives = 8\n")
    print("3. INSANE and the no. of lives =5\n")
    choice=int(input("give your choice by selecting a level "))
    if(choice==1):
        lives=10
        if(len(word)>10):
            print("choose other level the number of letters are more than 10")
    elif(choice==2):
        lives=8
        if(len(word)>8):
            print("choose another level the word is greater than 8 letters ")
    elif(choice==3):
        lives=5
        if(len(word)>5):
            print("you need more guesses the word is greater than 5 letters ")
    
    

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        #this is list comprehension :
        # so basically this means if the letter is in used_letters print letter or if it is not then print - a gap saying this is not there 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
