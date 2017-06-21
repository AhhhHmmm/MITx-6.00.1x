import string

def playGame():
	remainingLetters = list(string.ascii_lowercase)

	word = 'Xylophone'
	word = word.lower()
	skeleton = '_ '*len(word)
	playing = True
	usedLetters = []
	remGuesses = 8
	
	print('\n')
	print('*'*80)
	print('You have {} guesses to start.'.format(remGuesses))
	print('Remaining letters:', remainingLetters)
	print('The mystery word has {} letters.'.format(len(word)))
	print(skeleton)
	while playing:
		print('\n')
		print('*'*80)
		if remGuesses < 1:
			print('Sorry, you used all of your guesses.')
			print('GAME OVER\n\n')
			playing = False
			break
		print('Remaining letters:', remainingLetters)
		guess = input('Guess a letter: ')
		while not guess.isalpha() or len(guess) > 1:
			print('Please follow directions.')
			print(skeleton, '\n')
			print('Remaining letters:', remainingLetters)
			guess = input('Guess ONE letter: ')
		while guess in usedLetters:
			print('You\'ve already guessed \'{}\', please choose another letter.'.format(guess))
			print(skeleton, '\n')
			print('Remaining letters:', remainingLetters)
			guess = input('Guess a letter you have not guessed: ')
		if word.find(guess) == -1:
			print('\'{}\' is not in the word. You lose a guess.'.format(guess))
			remGuesses -= 1
			usedLetters.append(guess)
			remainingLetters.remove(guess)
			print('You have {} guesses remaining.'.format(remGuesses))
			print(skeleton)
		else:
			positions = []
			skeleton = list(skeleton)
			for index in range(len(word)):
				if word[index] == guess:
					skeleton[index*2] = guess
			skeleton = ''.join(skeleton)
			usedLetters.append(guess)
			remainingLetters.remove(guess)
			print('In word!!!')
			print(skeleton)
		if ''.join(skeleton.split(' ')) == word:
			print('You win!!!!\n\n')
			playing = False

playGame()
