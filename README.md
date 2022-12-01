# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The first task was to tackle the "computer thinks of  word", to do this i created a variable named "word_list"  and assigned it to a list of words, and printed to test. the computer then needs to select a word at random, to do this i imported the "random" function, called the "random.choice" function act on the "word_list"" and assigned the output to a new variable named "word".

the next step was promting user input, and verifying it met the specifications, as this is hangman, the specification is that the guess be 1 character and alphabtic in nature. i used an if statement and called the "len" funtion is equal to 1 and the "isalpha" numeric funtioned combined together, to either "good guess" or "Oops! That is not a valid input".