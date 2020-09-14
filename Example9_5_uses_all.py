#def uses_only(line, custom_symbols):
'''check a string-line contain custom only symbols'''
#	for letters in line:
#		if letters not in custom_symbols:
#			return False
#	return True

#def uses_all(line, all_symbols):
#	'''author solution using previous function uses_only'''
#	return uses_only(all_symbols, line)

'''Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many 
words are there that use all the vowels aeiou? How about aeiouy?'''

def uses_all(line, required):
	'''check a string-line contain all symbols at least once'''
	for letters in required:					
		if letters not in line:
			return False
	return True

def some_sort_words(filename):
	'''print and calculate words without broken symbols'''
	count = 0
	with open(filename) as f_open_file:
		for line in f_open_file:
			word = line.strip()
			if uses_all(word, required):
				print(word)
				count += 1
	return count


if __name__ == '__main__':	
	s = 'words.txt'
	required = input('input all needed symbols: ')
	print(some_sort_words(s))