def is_abecederian_for(word):
	''' letters in a word appear in alphabetical order 
	(double letters are ok) and number of abecederian words'''
	previous = word[0]
	for letters in word:					
		if letters < previous:
			return False
		previous = letters
	return True

def is_abecederian_recurse(word):
	if len(word) <= 1:
		return True
	if word[0] > word[1]:
		return False
	return is_abecederian_recurse(word[1:])

def is_abecederian_while(word):
	i = 0
	while i < len(word) - 1:
		if word[i+1] < word[i]:
			return False
		i += 1
	return True

def some_sort_words(filename):
	'''print and calculate words without broken symbols'''
	count = 0
	with open(filename) as f_open_file:
		for line in f_open_file:
			word = line.strip()
			if is_abecederian_recurse(word):
				print(word)
				count += 1
	return count


if __name__ == '__main__':	
	s = 'words.txt'	
	print(some_sort_words(s))