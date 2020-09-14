def is_palindrome(word):
    if word == word[::-1]:
        return True


def palindr_odometr():
    '''6 - digit in numbers last 4 digits were palindromic 
    One mile later, the last 5 numbers were palindromic. 
    One mile after that, the middle 4 out of 6 numbers were palindromic. 
    One mile later, all 6 were palindromic! 
    what was on the odometer when I first looked? 
    Write a Python program that tests all the six-digit numbers and 
    prints any numbers that satisfy these requirements'''
    for i in range(10**5, 10**6):
        temp_odometr6 = str(i)
        temp_odometr_m = str(i - 1)[1:-1]
        temp_odometr5 = str(i - 2)[1:]
        temp_odometr4 = str(i - 3)[2:]
        if is_palindrome(temp_odometr6) and is_palindrome(temp_odometr_m) and (
            is_palindrome(temp_odometr5) and is_palindrome(temp_odometr4)):             
            print(i - 3)    #defined position of odometr by this task
    

if __name__ == '__main__':  
	#print('possible digits are:') #interesting bug
    palindr_odometr()
    
