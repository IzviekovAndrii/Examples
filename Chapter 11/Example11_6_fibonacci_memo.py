import timeit

def fibonacci_original(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

#known = {0:0, 1:1}  
#If a global variable refers to a mutable value, you can modify the value without declaring the variable.
def fibonacci(n):
	if n in known:
		return known[n]
	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res
	return res

def check_time(f, number):
	start = timeit.default_timer() #reason time.time() do something else on Win10 and Py3.8
	#print('result calculation fibsum=', f(number))
	f(number)
	end = timeit.default_timer()
	return "{:.10f}".format(end - start)


if __name__ == '__main__':
	known = {0:0, 1:1}
	print()
	print('time fibonacci_original n=10 ', check_time(fibonacci_original, 10))
	print('time fibonacci n=10 ', check_time(fibonacci, 10))
	print()
	print('time fibonacci_original n=100 ', check_time(fibonacci_original, 100))
	print('time fibonacci n=100 ', check_time(fibonacci, 100))
	print()
	print('time fibonacci_original n=500 ', check_time(fibonacci_original, 500))
	print('time fibonacci n=500 ' , check_time(fibonacci, 500))
	print()
	print('time fibonacci_original n=990 ', check_time(fibonacci_original, 990))
	print('time fibonacci n=990 ' , check_time(fibonacci, 990))


