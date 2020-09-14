def has_no_e(word):
	'''check symbol "e" in word'''	
	if 'e' not in word:
		print(word)
		
		return True	

def calculate_no_e(filename):
	'''print words withot "e" and >20 symbols
	and calculate % to all'''
	index = 0
	no_e_index = 0
	with open(filename) as f_open_file:
		for line in f_open_file:
			word = line.strip()		
			if len(word) > 20:
				if has_no_e(word): 
					no_e_index += 1							
			index += 1
	print(no_e_index)
	print(index)

	return no_e_index / index


if __name__ == '__main__':	
	s = 'words.txt'
	print(calculate_no_e(s))