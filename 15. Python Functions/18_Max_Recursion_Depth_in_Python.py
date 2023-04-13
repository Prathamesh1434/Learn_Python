# recursion depth for recursion fn is 995

count = 0

def factorial(n):
	global count
	count += 1
	print('execution of factorial function for n =',n )
	if n==0:
		result = 1
	else:
		result = n*factorial(n-1)
	return result

print('Factorial of 994 =>',factorial(994))
print('Count of Factorial function executed =>',count)
# print('Factorial of 995 =>',factorial(995)) => RecursionError: maximum recursion depth exceeded while calling a Python object