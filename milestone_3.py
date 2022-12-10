word_list = ["banana","pear","apple","grape","mango","watermelon","strawberry","lychee"]
#randomly select a word

import random
word = random.choice(word_list)


def ask_for_input():

    guess = ""

    while True:
     guess = input(" Enter a single letter: ")

     if len(guess) == 1 and guess.isalpha():
         return guess

     else:
         print("Invalid letter. Please, enter a single alphabetical character.")
         continue


def check_guess(guess):
    if guess in word :
     print (f'Good guess! {guess} is in the word.')
     
    else:
     print (f'Sorry, {guess} is not in the word. Try again.')


guess = ask_for_input()
guess = guess.lower()
check_guess(guess)