def three_consecutive_double_letters(line):
	i = 0
	if len(line) >= 6:
		while i <= len(line) - 1 - 5:
			if line[i+1] == line[i] and line[i+3] == line[i+2] and line[i+5] == line[i+4]:				
				return True
			i = i + 1
		return False

'''def is_triple_double(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count
            count = 0
    return False'''	

def some_sort_words(filename):
	'''print and calculate words without broken symbols'''
	count = 0
	with open(filename) as f_open_file:
		for line in f_open_file:
			word = line.strip()
			if three_consecutive_double_letters(word):
				print(word)
				count += 1
	return count

if __name__ == '__main__':	
	s = 'words.txt'	
	print(some_sort_words(s))