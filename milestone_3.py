#milestone 3 leggo! 
# looping code that keeps asking user for input and validating
#must be one character long and a letter of the alphabet
#%%
guess = input("Enter your guess")
while not (len(guess)==1 and str.isalpha(guess)):
  guess = input("Invalid letter. Please, enter a single alphabetical character")
 




# %%
