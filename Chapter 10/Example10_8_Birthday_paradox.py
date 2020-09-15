import random
import Example10_7_has_duplicates

def Birthday_paradox():
	'''If there are 23 students in your class, what are the chances that two of you have 
	the same birthday? You can estimate this probability by generating random samples
	of 23 birthdays and checking for matches. Hint: you can generate random birthdays 
	with the randint function in the random	module
	p(n) = 1 - 365!/((365 - n)!*(365**n))
	making '100' lists containing 23 members '''
	count = 0
	for p in range(100): # approximation of probability p 
		t = []
		for i in range(n): # generation of birthdays
			t.append(random.randint(1, 365))
		if Example10_7_has_duplicates.has_duplicates(t):
			count += 1
	return count/100  # probability of chances by statistic 


if __name__ == '__main__':	
	n = 23
	print(Birthday_paradox())