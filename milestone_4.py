import random
class Hangman:
    
    def __init__(self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.list_of_guesses = []
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = list(self.word.replace(self.word[0:], "_"* (len(self.word))))
        self.num_list = "".join(set(self.word)).lower()
        self.num_letters = len(set(self.word))

    
    def ask_for_input(self):
        guess = ""
        while True:
            guess = input(" Enter a single letter: ")
            if len(guess) != 1 or guess.isnumeric():
                 print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                 print ("You already tried that letter!.")
            else:
                 self.check_guess(guess)
                 break
                 

    
    def check_guess(self,guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)
            


game2 = Hangman(["banana","pear","apple","grape","mango","watermelon","strawberry","lychee"])
print(game2.word_guessed)
type(game2.word_guessed)
print(game2.word)
print(game2.num_letters)

