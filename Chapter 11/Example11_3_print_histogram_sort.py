import Example11_2_histogram

def print_hist(h):
	for c in h:
		print(c, h[c])

def print_hist_sort(h):
	'''sorted histogram by keys'''
	for key in sorted(h): #sorted is inbound method for dictionary keys
		print(key, h[key])



if __name__ == '__main__':  
	s = 'parrot'
	h = Example11_2_histogram.histogram(s)
	print_hist(h)
	print()
	print_hist_sort(h)