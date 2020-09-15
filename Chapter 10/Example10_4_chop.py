def chop(t):
	'''Write a function called chop that takes a list, modifies it by removing the first and
	last elements, and returns None.'''
	del t[0]
	del t[-1]


if __name__ == '__main__':
	t = [1, 2, 30, 400, 5000]
	print(t)
	print(chop(t))
	print(t)