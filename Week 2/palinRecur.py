word = 'oHahO'

def processWord(word):
	tempWord = ''
	for letter in word:
		if letter.isalpha():
			tempWord += letter
	tempWord = tempWord.lower()
	return tempWord

def palinRecur(word):
	if len(word) == 0 or len(word) == 1:
		return True
	else:
		return word[0] == word[-1] and palinRecur(word[1:-1])

print(palinRecur(processWord('ohO')))