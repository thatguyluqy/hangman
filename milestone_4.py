
class Hangman:
    
    def __init__(self,word_list,num_lives=5):
        import random
        self.word = random.choice(word_list)
        self.list_of_guesses = []
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = self.word.replace(self.word[0:], "\"-\","* (len(self.word)))
        self.num_list = "".join(set(self.word)).lower()

    
    def ask_for_input(self):
        guess = ""
        while True:
            self.guess = input(" Enter a single letter: ")
            if len(guess) == 1 and guess.isalpha():
                 return guess
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
game2.ask_for_input()