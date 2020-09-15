def nested_sum(t):
	'''Write a function called nested_sum that takes a list of lists of integers and adds up
	the elements from all of the nested lists'''
	#nt = []
	nestsum = 0
	for i in range(len(t)):
		if isinstance(t[i], list):
			nestsum += nested_sum(t[i])
		else:
			nestsum += t[i]
	return nestsum

if __name__ == '__main__':
	t = [[1, 2], [3, 50, 100], [4, 5]]
	print(nested_sum(t))
