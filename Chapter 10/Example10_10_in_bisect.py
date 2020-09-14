def make_list(filenametxt):
    t =[]
    with open(filenametxt) as f:
        for line in f:          
            word = line.strip()
            t.append(word)  
    return t

def in_bisect(t, word):
    '''Because the words are in alphabetical order, we can speed things up with a 
    bisection search (also known as binary search) You start in the middle and check 
    to see whether the word you are looking for comes before the word in the middle 
    of the list. If so, you search the first half of the list the same way. Otherwise 
    you search the second half.
    Write a function called in_bisect that takes a sorted list and a target value and 
    returns True if the word is in the list and False if it’s not'''
    #t = list(sort_t)
    #Напишите функцию bisect, которая принимает отсортированный список и искомое значение,  
    #и возвращает индекс этого значения в списке либо None, если его там нет.
    width = len(t)

    if width == 0:
        return False
    else:        
        sep_pos = width // 2
        sep_elem = t[sep_pos]
        if sep_elem == word:            
            return True                                             
        if word < sep_elem:
            nt = t[:sep_pos]        
            return in_bisect(nt, word) 
        elif word > sep_elem:
            nt = t[sep_pos + 1:]        
            return in_bisect(nt, word)
 

if __name__ == '__main__':  
    s = 'words.txt' 
    your_word = input('input a searching word: ')
    sorted_t = make_list(s)
    small_t = make_list(s)[:10:2]
    print(small_t)
    #print(in_bisect(sorted_t, your_word))
    print(in_bisect(small_t, your_word))