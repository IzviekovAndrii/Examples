def cumsum(t):
	'''Write a function called cumsum that takes a list of numbers and returns
	the cumulative sum; that is, a new list where the ith element is
	the sum of the first i + 1 elements from the original list'''
	ct = []
	new_el = 0
	for i in range(len(t)):
		new_el += t[i] 
		ct.append(new_el)
	return ct 


if __name__ == '__main__':
	t = [1, 2, 30, 400, 5000]
	print(t)
	print(cumsum(t))