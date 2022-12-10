word_list = ["banana","pear","apple","grape","mango","watermelon","strawberry","lychee"]
#randomly select a word

import random
word = random.choice(word_list)

guess = ""

while True:
    guess = input("Enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
        print(guess)
        break

    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        continue
if guess in word :
    print ( "Good guess! {guess} is in the word.")
else:
    print ("Sorry, {guess} is not in the word. Try again.")