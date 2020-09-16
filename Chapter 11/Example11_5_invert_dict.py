import Example11_2_histogram

def invert_dict_old(d):
	'''Inverts a dictionary. Since there might be several letters with the same
	frequency, each value in the inverted dictionary should be a list of letters.'''
	inv = dict()
	for key in d:
		val = d[key]
		if val not in inv:
			#create a new item and initialize it with a singleton 
			#(a list that contains a single element)
			inv[val] = [key]     
		else:
			inv[val].append(key)
	return inv

def invert_dict(d):
	'''Inverts a dictionary. Each value in the inverted dictionary should be a list of letters.
	use "setdefault" to modify invert_dict_old'''
	#dict.setdefault(key, default = None)
	#key − это ключ для поиска.
	#default − это значение, которое будет возвращено в случае, если ключ будет не найден.
	inv = dict()
	for key in d:
		val = d[key]
		inv.setdefault(val, [])		  		
		inv[val].append(key)
	return inv


if __name__ == '__main__':
	s = 'parrot'
	d = Example11_2_histogram.histogram(s)
	print(d)
	inv_old = invert_dict_old(d)
	print('inv_old = ', inv_old)
	inv = invert_dict(d)
	print('inv = ', inv)
