import random
word_list = ["banana","pear","apple","grape","mango","watermelon","strawberry","lychee"]
word = random.choice(word_list)

def ask_for_input():

    guess = ""

    while True:
     guess = input(" Enter a single letter: ")
     if len(guess) == 1 and guess.isalpha():
        check_guess(guess)
        break
     
     else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        continue


def check_guess(guess):
    guess == guess.lower()
    if guess in word :
     print (f'Good guess! {guess} is in the word.')
     
    else:
     print (f'Sorry, {guess} is not in the word. Try again.')


guess = ask_for_input()
