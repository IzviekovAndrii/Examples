import Example10_10_in_bisect 

def reverse(word):
	return word[::-1]

def reverse_pair(t):
	'''Two words are a “reverse pair” if each is the reverse of the other. 
	Write a program	that finds all the reverse pairs in the word list'''
	
	'''for word in t:
		if reverse(word) in t:
			print(word, reverse(word))'''
			# работает, но медленнно при большом списке
	for word in t:
		if Example10_10_in_bisect.in_bisect(t, reverse(word)):
			print(word, reverse(word))  


if __name__ == '__main__':	
	s = 'words.txt'
	t = Example10_10_in_bisect.make_list(s)
	small_t = Example10_10_in_bisect.make_list(s)[::10] # make list whith lenth 10 time smaller original
	reverse_pair(small_t)
