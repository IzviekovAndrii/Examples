'''def do_twice(f):
	f()
	f()
	
def print_spam():
    print('spam')
	
do_twice(print_spam)
'''
s = input('input string: ')

def do_twice(function, a):
    function(a)
    function(a)

def print_twice(a):
    print(a)
    print(a)

def do_four(function, a):
    do_twice(function, a)
    do_twice(function, a)

do_twice(print_twice, s)   #первая часть из 4 пунктов

print('')

do_four(print, s)          #пункт 5  

