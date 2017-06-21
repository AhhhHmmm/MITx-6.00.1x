import string

def isWordGuessed(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: boolean, True if all the letters of secretWord are in lettersGuessed,
		False otherwise
	'''
	guessed = True
	for letter in secretWord:
		if letter not in lettersGuessed:
			guessed = False
			break
	return guessed

def getGuessedWord(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters and underscores that represent
		what letters in secretWord have been guessed so far
	'''
	displayedWord = ''
	for letter in secretWord:
		if letter in lettersGuessed:
			displayedWord += letter
		else:
			displayedWord += '_ '
	return displayedWord

def getAvailableLetters(lettersGuessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not yet been guessed.
	'''
	allLetters = list(string.ascii_lowercase)
	for letter in lettersGuessed:
		try:
			allLetters.remove(letter)
		except ValueError:
			pass
	return ''.join(allLetters)

def getGuess(secretWord, remainingGuesses, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	remainingGuesses: int, number of guesses remaining
	lettersGuessed: list, what letters have been guessed so far

	prints a variety of alerts, telling the user how many letters remaining, what letters available
	and then prompts the user for a guess.

	verifies the guess is a new guess (the letter has not been guessed before)

	returns the guessed character
	'''
	dividerString = '-'*13

	# print information to the screen regarding available letters and remaining guesses
	print(dividerString)
	print('You have {} guesses left.'.format(remainingGuesses))
	print('Available letters:', getAvailableLetters(lettersGuessed))

	# prompt the user for a guess
	guess = input('Please guess a letter: ')
	guess = guess.lower() # make sure the guess is lower case

	if guess in lettersGuessed:
		print('Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
		# recursively calls itself if the previous guess was not new
		guess = getGuess(secretWord, remainingGuesses, lettersGuessed)
	return guess

def hangman(secretWord):
	'''
	secretWord: string, the secret word to guess.

	Starts up an interactive game of Hangman.

	* At the start of the game, let the user know how many letters the secretWord contains.

	* Ask the user to supply one guess (i.e. letter) per round.

	* The user should receive feedback immediately after each guess about whether their 
		guess appears in the word.

	* After each round, you should also display to the user the partially guessed word so far
		as well as letters that the user has not yet guessed.

	Follows the other limitations in the problem write-up.
	'''
	
	secretWord = secretWord.lower()
	wordLength = len(secretWord)
	remainingGuesses = 8
	playing = True
	lettersGuessed = []

	print('Welcome to the game, Hangman!')
	print('I am thinking of a word that is {} letters long.'.format(wordLength))

	while playing:
		guess = getGuess(secretWord, remainingGuesses, lettersGuessed)
		lettersGuessed.append(guess)
		if guess in secretWord:
			print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
		else:
			remainingGuesses -= 1
			print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
		if isWordGuessed(secretWord, lettersGuessed):
			dividerString = '-'*13
			print(dividerString)
			print('Congratulations, you won!')
			playing = False
			break
		if remainingGuesses < 1:
			dividerString = '-'*13
			print(dividerString)
			print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
			playing = False
			break

secretWord = 'apple'
hangman(secretWord)

