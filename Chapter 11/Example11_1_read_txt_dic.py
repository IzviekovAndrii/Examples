import Example10_10_in_bisect
import timeit 

def make_dic(filenametxt):
	'''Write a function that reads the words in words.txt and stores them as keys in a
	dictionary. It doesn’t matter what the values are. Then you can use the in operator as 
	a fast way to check whether a string is in the dictionary.
	If you did Exercise 10.10, you can compare the speed of this implementation with the list in operator and the bisection search.'''
	d = dict()
	with open(filenametxt) as f:
		for line in f:          
			word = line.strip()
			d[word] = '1'
	return d

def check_time(f, par, word):
	start = 0
	start = timeit.default_timer() #reason time.time() do something else on Win10 and Py3.8
	if f(par, word):			
		print('Have this word')
	else:
		print('Havnt this word')	
	end = timeit.default_timer()
	return "{:.16f}".format(end - start)

def in_dic(d, word):
	if	word in d:
		return True
	

def in_list(t, word):
	if word in t:
		return True
	

if __name__ == '__main__':  
    s = 'words.txt' 
    your_word = input('input a searching word: ')
    d = make_dic(s)
    t = Example10_10_in_bisect.make_list(s) #common function using append method
    print('time search in dictionary', check_time(in_dic, d, your_word))
    print('time search in list bisect', check_time(Example10_10_in_bisect.in_bisect, t, your_word))
    print('time search in list', check_time(in_list, t, your_word))



