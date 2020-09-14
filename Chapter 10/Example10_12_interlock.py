import Example10_10_in_bisect
import Example9_5_uses_all

def interlock(word1, word2, word3):
	'''Two words “interlock” if taking alternating letters from each forms a new
	word. For example, “shoe” and “cold” interlock to form “schooled”. 
	1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate 
	all pairs! 
	2. Can you find any words that are three-way interlocked; that is, every third letter 
	forms a word, starting from the first, second or third?'''
	if (len(word1) + len(word2)) != len(word3):
		return False
	else:
		t3 = word1 + word2
		if Example9_5_uses_all.uses_all(t3, word3):
			print(word1, word2, word3)

def interlock_finding(t):
	for i in range(len(t)):		
		for k in range(len(t)):			
			interlock(t[i], t[k], t[len(t) - 1 - i])

if __name__ == '__main__':	
	#s = 'words.txt'
	#t = Example10_10_in_bisect.make_list(s)
	t_my = ['arc', 'Andrey', 'cra', 'barcra', 'crarca', 'ra', 'rararara']	
	#interlock_finding(t)
	interlock_finding(t_my)

