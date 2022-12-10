
class Hangman:
    
    def __init__(self,word_list,num_lives=5):
        list_of_guesses = []
        import random
        self.word = random.choice(word_list)
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = self.word.replace(self.word[0:], "\"-\","* (len(self.word)))
        self.num_list = "".join(set(self.word)).lower()