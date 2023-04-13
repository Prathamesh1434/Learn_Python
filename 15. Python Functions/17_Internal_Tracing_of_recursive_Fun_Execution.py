def factorial(n):
	print('execution of factorial function for n =',n )
	if n==0:
		result = 1
	else:
		result = n*factorial(n-1)
	print('Returning factorial ({}) is : {}'.format(n,result))
	return result

print('Factorial of 4 =>',factorial(4))
