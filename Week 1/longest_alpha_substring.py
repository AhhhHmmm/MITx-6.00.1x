import string
alpha = string.ascii_lowercase

def find_longest_substring(s):
	longest_run = ''
	current_run = ''
	current_pos = 0
	while current_pos < len(s):
		if current_run == '':
			current_run = s[current_pos]
		elif alpha.index(current_run[-1]) <= alpha.index(s[current_pos]):
			current_run += s[current_pos]
		else:
			current_run = s[current_pos]
		current_pos += 1
		if len(current_run) > len(longest_run):
			longest_run = current_run
	return(longest_run)

print(find_longest_substring('familiarize'))