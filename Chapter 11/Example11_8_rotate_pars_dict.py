def make_dic(filenametxt):
	'''dictionry from txt file and key = "1" '''
	d = dict()
	with open(filenametxt) as f:
		for line in f:          
			word = line.strip()
			d[word] = '1'
	return d

def rotate_word(word, step):
	'''transform english alphabet symbols into new alphabet symbols with
	step line is words in line'''
	new_word = ' '		
	for symbol in word:		  
		if symbol.isupper():
			start = ord('A')
		else: 
			start = ord('a')	

		delta = ord(symbol) - start
		new_symbol = chr((delta + step) % 26 + start) # 26 is numbers of symbols
		new_word += new_symbol 
	return new_word

def rotate_pairs(d, step):
	'''Write a program that reads a wordlist and finds all the rotate pairs.'''	
	for word in d:
		
		new_word = rotate_word(word, step)	
		print(step, word, new_word)
		#import ipdb; ipdb.set_trace()

		if new_word in d:
			print('+++', word, new_word)
			print()
			#return True
	#return False
		
		


if __name__ == '__main__':
	#s = 'words.txt' 
	s = 'test_words.txt' 
	strw = 'rotate_pairs'
	d = make_dic(s)
	print(d)
	
	for step in range(1, 2): # 26 -> 2 
		rotate_pairs(d, step)
