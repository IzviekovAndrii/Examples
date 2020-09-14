def is_palindrome(word):
    if word == word[::-1]:
        return True

def  reverse(word):
    return word[::-1]

def reverse_age():
    '''the digits of our ages have been reversible six times so far. 
    It would have happened 8 times over all. So the question is, how old am I now? 
    Hint: you might find the string method zfill useful. str.zfill(width)'''
    count = 1 # count of palindrom age mappings    
    for i in range(10, 200):
        mother = str(i).zfill(2)        
        me = reverse(mother)
        dif = int(mother) - int(me) # 10 is minimum age of mother                  
        if dif > 10 and ((dif * 8) <= 200): # condition and reallife 200 = max age            
            if count == 6:
                print(mother, me, dif, count)
                return me 
            count += 1   #return dif


if __name__ == '__main__':
    r = reverse_age()
    print('now I have', r)