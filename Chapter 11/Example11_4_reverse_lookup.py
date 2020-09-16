import Example11_2_histogram

def reverse_lookup_single(d, v):
	'''takes a value and returns the first key that maps to that value v=d[k]'''
	for k in d:
		if d[k] == v:
			return k
	raise ValueError

def reverse_lookup(d, v):
	'''takes a value and returns the list of keys that maps to that value 
	or empty list if no keys that maps to that value'''
	t = []
	for k in d:
		if d[k] == v:
			t.append(k)			
	return t


if __name__ == '__main__':
	s = 'parrot'
	d = Example11_2_histogram.histogram(s) #creating dict as histogram of custom string
	print('all values whith key="0": ', reverse_lookup(d, 0))
	print('all values whith key="1": ', reverse_lookup(d, 1))
	print('all values whith key="2": ', reverse_lookup(d, 2))
	print('all values whith key="3": ', reverse_lookup(d, 3))
