# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The first task was to tackle the "computer thinks of  word", to do this i created a variable named "word_list"  and assigned it to a list of words, and printed to test. the computer then needs to select a word at random, to do this i imported the "random" function, called the "random.choice" function act on the "word_list"" and assigned the output to a new variable named "word".

the next step was promting user input, and verifying it met the specifications, as this is hangman, the specification is that the guess be 1 character and alphabtic in nature. i used an if statement and called the "len" funtion is equal to 1 and the "isalpha" numeric funtioned combined together, to either "good guess" or "Oops! That is not a valid input".

another piece of the puzzle is prompting the user repeatedly if they do not guess valid character, so to achieve this i created a while loop that stipulated aslong as the character entered is not a letter in the alphabet and not 1 character long the loop will keep prompting the user to enter a valid input, once the input is valid it is stored in the variable guess.

ive now included the word list and random word generator in the code. ive then added code to take the guessed letter and check if it is in the randomly generated word.

ive now defined a function to the guessed character validation code, and also a function to the check if guess is in word code, aswell as a line to convert the guess to lower case letters.

now the functions run in order of

1.select random word from list
2.store word in variable "word"
3.check users entered guess, ensure it is one character and alphabetical
3.store guessed letter in variable "guess"
4.convert guess to lower case
5.check to see if users guess is in variable "word"

Next i created the Hangman class to essentially convert the program in to an Object oriented program. I then used the __init__ method to initiate an instance of the class. i iniated multiple attributes of the class that would come into affect later.

word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.
word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].
num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
num_lives: int - The number of lives the player has at the start of the game.
word_list: list - A list of words.
list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

i created 2 methods within the class , one to ask for an input check the guess was a single alphabetical letter and another that checked if the guess was in the word, enumerate through the word to see if the letter was in the word and how many times, and then update the word guessed list to replace the blanks with the letter if it was correct everywhere the letter appeared whilst also removing the letter from the list of unique letters in the word (num_letters)

i also set logic within the method to return that the guess was not in the word if that was the case and reduce number of lives by one.

finally i created a function outide of the class that took in the word list as an argumant, started an instance of ther hangman class called game, and set the number of lives to 5. this funtion also would loop through to see if the number of lives hit 0 to inform the player they lost the game. if the number of lives was above zero this funtion would check if the number of unique characters in the word (num_letters) was equal to zero, if it wasnt it would keep prompting the user for guesses. if it was equal to zero it would mean the word was correctly guessed and the user had one the game.

all that was left to do was call the play_game function, pass the word list through and the game logic was complete!