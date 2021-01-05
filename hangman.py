# Write your code here
# First version
"""import random

words_list = ['python', 'java', 'kotlin', 'javascript']
survive_word = random.choice(words_list)
hint = survive_word[0: 3]
number_signs = len(survive_word) - 3
signs = "-" * number_signs

print("H A N G M A N")
word = input("Guess the word {}{}: ".format(hint, signs))

if word == survive_word:
    print('You survived!')
else:
    print('You lost!')"""

# Version 2.0
'''
import random

words_list = ['python', 'java', 'kotlin', 'javascript']
survive_word = random.choice(words_list)
number_signs = len(survive_word)
signs = list("-" * number_signs)
hint = "".join(signs)
print("H A N G M A N")

for _i in range(1, 9):
    print(f"\n{hint}")
    letter = input("Input a letter: ")


    if letter in survive_word:
        for position in range(len(survive_word)):
            if letter == survive_word[position]:
                signs.pop(position)
                signs.insert(position, letter)
        hint = "".join(signs)
    else:
        print("That letter doesn't appear in the word")

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
'''

# Version 3.0
'''import random

words_list = ['python', 'java', 'kotlin', 'javascript']
survive_word = random.choice(words_list)
number_signs = len(survive_word)
signs = list("-" * number_signs)
hint = "".join(signs)
lives = 8

print("H A N G M A N")

while lives > 0:
    print(f"\n{hint}")
    letter = input("Input a letter: ")

    if letter in survive_word:
        if letter in hint:
            lives -= 1
            print('No improvements')
        else:
            for position in range(len(survive_word)):
                if letter == survive_word[position]:
                    signs.pop(position)
                    signs.insert(position, letter)
        
        hint = "".join(signs)
    else:
        lives -= 1
        print("That letter doesn't appear in the word")

    if hint == survive_word:
        break


if lives == 0:
    print('You lost!')
else:
    print("\n" + survive_word)
    print('You guessed the word!')
    print('You survived!') '''

# Version 4.0

import random

words_list = ['python', 'java', 'kotlin', 'javascript']
survive_word = random.choice(words_list)
number_signs = len(survive_word)
signs = list("-" * number_signs)
hint = "".join(signs)
repeated_letters = []
lives = 8

def control_correct_format(letter, hint, repeated_letters, lives):

    if 1 < len(letter) or len(letter) == "":
        print("You should input a single letter")
        return True
    elif not(letter.isalpha()) or letter.isupper():
        print("Please enter a lowercase English letter")
        return True
    elif letter in hint or letter in repeated_letters:
        print("You've already guessed this letter")
        return True
    elif letter in survive_word:
        pass
    else:
        print(lives)
        print("That letter doesn't appear in the word")
        repeated_letters.append(letter)     
        return False

print("H A N G M A N")
lets_play = input('Type "play" to play the game, "exit" to quit:')


while lets_play == 'play':
    while lives > 0:
        print(f"\n{hint}")
        letter = input("Input a letter: ")
        control = control_correct_format(letter, hint, repeated_letters, lives)
        if control == True:
            pass
        elif control == False:
            lives -= 1
        else:
            if letter in survive_word:
                if letter not in hint:
                    for position in range(len(survive_word)):
                        if letter == survive_word[position]:
                            signs.pop(position)
                            signs.insert(position, letter)
                
                hint = "".join(signs)



            if hint == survive_word:
                break

    if lives == 0:
        print('You lost!')
    else:
        print(f'You guessed the word {survive_word}!')
        print('You survived!')
    lets_play = input('Type "play" to play the game, "exit" to quit:')


