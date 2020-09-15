def middle(t):
	'''Write a function called middle that takes a list and returns a new list that contains
	all but the first and last elements'''
	return t[1: -1]


if __name__ == '__main__':
	t = [1, 2, 30, 400, 5000]
	print(t)
	print(middle(t))
