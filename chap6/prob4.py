HANGMAN_PICS = ['''
  ------
  |    
  |   
  |    
  |  
  |
----------''', ''' 
  ------
  |    O  
  |  
  |   
  |
  |
----------''', '''
  ------
  |    O  
  |    +
  |   
  |
  |
----------''', '''
  ------
  |    O  
  |   -+
  |   
  |
  |
----------''', '''
  ------
  |    O  
  |   -+-
  |   
  |
  |
----------''', '''
  ------
  |    O  
  |   -+-
  |    |
  |   /
  |
----------''', '''
  ------
  |    O  
  |   -+-
  |    |
  |   / \
  |
----------''', '''
  ------
  |   [O  
  |   -+-
  |    |
  |   / \
  |
----------''', '''
  ------
  |   [O]  
  |   -+-
  |    |
  |   / \
  |
----------''']

word_to_guess = "python"

guessed_word = ["_"] * len(word_to_guess)
incorrect_guesses = 0

guessed_letters = set()

while True:
    print(HANGMAN_PICS[incorrect_guesses])

    print(" ".join(guessed_word))

    guessed_letters_str = " ".join(guessed_letters)
    if guessed_letters_str:
        print("You've used the following letters:", guessed_letters_str)

    guess = input("Enter your guess: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_word[i] = guess
        print(f"Yes! '{guess}' is in the word!")
    else:
        incorrect_guesses += 1

    if "".join(guessed_word) == word_to_guess:
        print("Congratulations! You've guessed the word:", word_to_guess)
        break
    elif incorrect_guesses == len(HANGMAN_PICS) - 1:
        print("Sorry, you've run out of guesses. The word was:", word_to_guess)
        break

