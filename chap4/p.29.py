import random
print('    welcom to Guess My Number\n')
print('I am thinking of a number between 1 and 100.\n Try to guess it few attnepts as possible.')

answer = random.randrange(1,100)
count = 0
while True:
	count +=1
	number = int(input('Take a guess: '))
	if number > answer:
	   print('Lower...')
	elif number < answer:
	   print('Higher...')
	else:
	   print('You guess it! THe number was', answer,'And it only took',count,'tries!')
	   break
