def avoids(line, broken_symbols):
	'''check existense broken symbols in string-line'''
	for letters in line:
		if letters in broken_symbols:
			return False
	return True

def some_sort_words(filename):
	'''print and calculate words without broken symbols'''
	count = 0
	with open(filename) as f_open_file:
		for line in f_open_file:
			word = line.strip()
			if avoids(word, broken_symbols):
				print(word)
				count += 1
	return count

def minimum():
	'''Can you find a combination of 5 forbidden letters
	that excludes the smallest number of words?
	Можете ли вы найти такую комбинацию	из 5 запрещенных букв, 
	которые	выводят	наименьшее число слов в	вашей программе?'''
	pass

if __name__ == '__main__':	
	s = 'words.txt'
	broken_symbols = input('input avoided(broken) symbols: ')
	print(some_sort_words(s))