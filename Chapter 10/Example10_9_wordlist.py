import time

def wordlist1(filenametxt):
	'''Write a function that reads the file words.txt and builds a list with one element
	per word. Write two versions of this function, one using the append method and the 
	other using the idiom t = t + [x]. Which one takes longer to run? Why?'''

	#answer: the append method modifies a list, but the + operator creates a new list
	
	start = time.time()
	print(start)
	t = []
	with open(filenametxt) as f:
		for line in f:			
			word = line.strip() # del '\n' both sides string 
			t = t + [word]
	end = time.time()
	print(end)
	return end - start	

def wordlist2(filenametxt):
	start = time.time()
	print(start)
	t = []
	with open(filenametxt) as f:
		for line in f:			
			word = line.strip() # del '\n' both sides string 
			t.append(word)
	end = time.time()
	print(end)
	return end - start	


if __name__ == '__main__':	
	s = 'words.txt'
	print('waiting for ending program, full time words.txt is about 3 min')
	print('working time function whith "+" = ', wordlist1(s))
	print('working time function whith "append" = ', wordlist2(s))