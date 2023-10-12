import random
print('Welcome to Word Jumble!')
print('Unscramble the letters to make a word.')
word=('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
a=random.choice(word)
jumble=''.join(random.sample(a,len(a)))
print('Jumble word:',jumble)
guess=input('Your guess: ')
if guess==a:
	print("That's correct")
else:
	print("Sorry, that's not correct. The word was:",a)
