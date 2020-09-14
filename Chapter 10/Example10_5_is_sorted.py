def is_sorted(t):
	'''Write a function called is_sorted that takes a list as a parameter and returns True
	if the list is sorted in ascending order and False otherwise'''
	temp = t[0]
	for i in range(len(t)):				
		if t[i] >= temp:
			temp = t[i]			
		else:
			return False
		i += 1
	return True

if __name__ == '__main__':
	t = [1, 200, 300, 40, 5000]
	print(t)
	print(is_sorted(t))
