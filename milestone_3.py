while True:
    guess = input("Enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
        print(guess)
        break

    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        continue

