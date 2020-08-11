#Напишите	функцию	right_justify	(выровнять	по	правому	краю),	которая	берет	строку	s	в	качестве	
#параметра	и	печатает	ее	так,	чтобы	оставить	с	левой	стороны	столько	пробелов,	чтобы	последняя	буква	
#была	на	70-й	позиции.
s = input('input string: ')

def right_justify(a):
    if len(a)<=70:
        print((' ')*(70-len(a)), a, sep='')        
    else:
        print('Your string so long, enter new: ')

right_justify(s)
	