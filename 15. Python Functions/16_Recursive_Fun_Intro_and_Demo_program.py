# Recursive Function
# Solve complex funxtion easily
# Length will be reduced , and readiblity improve.

# Ex - Factorial
# Without recursion

# n = 3 >=1
# result = 1 * 3 = 3
# n = 2 >=1
# result = 3 * 2 = 6
# n = 1 >=1
# result = 6 * 1 = 6

def fact(n):
	result=1
	while n>=1:
		result = result * n
		n=n-1
		return result

# With recursion
# 3! = 3 * 2!
#	 = 3 * 2 * 1!
#    = 3 * 2 * 1 * 0!
#    = 3 * 2 * 1 * 1 = 6
# n! = n * (n-1)!
# fact(n)=n*fact(n-1)
def factorial(n):
	if n==0:
		result = 1
	else:
		result = n*factorial(n-1)
	return result

print('Factorial of 4 =>',factorial(4))


for i in range(11):
	print('Factorial of {} => {}'.format(i,factorial(i)))