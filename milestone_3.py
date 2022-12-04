#milestone 3 leggo! 
# looping code that keeps asking user for input and validating
#must be one character long and a letter of the alphabet

#%%
guess = ""

while True:
    guess = input("Enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
        print(guess)
        break

    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        continue



# %%
