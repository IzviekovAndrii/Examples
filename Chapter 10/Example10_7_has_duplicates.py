def has_duplicates(t):
	'''Write a function called has_duplicates that takes a list and returns True 
	if there is any element that appears more than once. It should not modify 
	the original list'''
	nt = t[:]	
	for elements in range(len(nt)):
		temp = nt[0]
		nt.remove(nt[0])
		if temp in nt:
			return True
	return False	


if __name__ == '__main__':	
	a = [1, 2, 'a', 'aa', [1], '1a', 1]
	b = [1, 2, 'a', 'aa', [1], '1a']
	print(a)
	print(b)	
	print('a', has_duplicates(a))
	print('b', has_duplicates(b))