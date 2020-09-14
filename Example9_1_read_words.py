def read_words(filename):
	'''print words > 20 symbols''' 
	f_open_file = open(filename)
	for line in f_open_file:
		word = line.strip()
		if len(word) > 20:	
			print(word)
	f_open_file.close()

if __name__ == '__main__':	
	s = 'words.txt'
	read_words(s)