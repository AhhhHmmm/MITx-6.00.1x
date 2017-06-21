def playGame():
	playing = True
	low = 0
	high = 100
	print('Please think of a number between 0 and 100!')
	while playing:
		guess = int((low + high)/2)
		print("Is your secret number {}".format(guess))
		feedback = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
		if feedback == 'c':
			playing = False
		elif feedback == 'l':
			low = guess
		elif feedback == 'h':
			high = guess
		else:
			print('Sorry, I did not understand your input.')
	print('Game over. Your secret number was: {}'.format(guess))

playGame()