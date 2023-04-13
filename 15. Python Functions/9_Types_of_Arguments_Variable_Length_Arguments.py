# Variable Length Arguments
# f1(*n) => *n => Variable length argument. => We can pass any number of argument.

def f1(*n): # Type on n => Tuple
	print('n => ',n)
	print('Type of n => ',type(n))
	print('Variable length argument function.')

f1() # n = ()
f1(10) # n = (10,)
f1(10,20,30) # n = (10,20,30)
f1((10,20),(24,30,40))

# Find the sum of the numbers.
def sum(*n):
	sum = 0
	for x in n:
		sum += x
	print('The Sum => ',sum)

sum(10,20)
sum(10,20,30,40)
sum()