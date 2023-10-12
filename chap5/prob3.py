print ('Guess the Word!!!')
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.")
import random
words=('difficult', 'banana', 'apple', 'python', 'daegu', 'cathoic', 'university')
word=random.choice(words)
guesses=''
print('Length of select word: ',len(word))
attempts=6
print("Remaining attempts : ", attempts)

while True:
   success = True
   print("Current guessed word :", end="")
   for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print(' _ ', end='')
            success = False
   print()
    
   if success:
        print("\nCongr")
        break;
        
   guess = input("\nGuess a letter:")
   if guess not in guesses:
     guesses += guess

   if guess in word:
    print("Correct")
    print("Remaing -  selected word :",attempts)
   else:
    attempts = attempts -1
    print("incorrect guess")
    print("Remaing -  selected word", attempts)
   if attempts == 0:
    print("you used attemps. correct word :", word)
    break;
