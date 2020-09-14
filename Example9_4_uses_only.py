def uses_only(line, custom_symbols):
	'''check a string-line contain custom only symbols'''
	for letters in line:
		if letters not in custom_symbols:
			return False
	return True

def some_sort_words(filename):
	'''print and calculate words without broken symbols'''
	count = 0
	with open(filename) as f_open_file:
		for line in f_open_file:
			word = line.strip()
			if uses_only(word, custom_symbols):
				print(word)
				count += 1
	return count



if __name__ == '__main__':	
	s = 'words.txt'
	custom_symbols = input('input custom only symbols: ')
	print(some_sort_words(s))