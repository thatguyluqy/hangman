import random
class Hangman:
    
    def __init__(self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.list_of_guesses = []
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = list(self.word.replace(self.word[0:], "_"* (len(self.word))))
        self.num_list = "".join(set(self.word)).lower()

    
    def ask_for_input(self):
        guess = ""
        while True:
            self.guess = input(" Enter a single letter: ")
            if len(self.guess) != 1 or self.guess.isnumeric():
                 print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                 print ("You already tried that letter!.")
            else:
                 self.check_guess(guess)
    
    def check_guess(self,guess):
        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word.")
        else:
            print(f"sorry {self.guess} isnt in the word")


game2 = Hangman(["banana","pear","apple","grape","mango","watermelon","strawberry","lychee"])
print(game2.word_guessed)