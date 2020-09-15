def is_anagram(a, b):
	'''Two words are anagrams if you can rearrange the letters from one
	to spell the other.	Write a function called is_anagram that takes
	two strings and returns True if they are anagrams'''
	t1 = list(a)
	t2 = list(b)
	
	'''if len(t1) != len(t2):
		return False	
	else:
		while len(t1) >= 1:
			temp = t1[0]
			if temp in t2:
				t1.remove(temp)
				t2.remove(temp)
			else:
				return False
	return True'''
	if len(t1) != len(t2):
		return False
	else:
		for items in range(len(t1)): 
			if t1[items] not in t2:
				return False
			else:	
				temp = t1[items]
				t2.remove(temp)
	return True

if __name__ == '__main__':
	a = 'armada'
	b = 'daarmi'
	print(a, b, is_anagram(a, b))