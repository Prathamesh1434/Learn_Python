# Creation of Tuple
t = ()
print('Tuple t => ',t)
t = (10,)
print('Tuple t => ',t)
t = (10,20,30)
print('Tuple t => ',t)
t = 10,20,30
print('Tuple t => ',t)
t = (10,20,30,)
print('Tuple t => ',t)
t = 10,20,30,
print('Tuple t => ',t)

# By using tuple function.
l = [10,20,30]
t = tuple(l)

t = tuple(range(1,11,2))
print('Tuple t => ',t)

t = tuple('Prathmesh')
print('Tuple t => ',t)

# With dynamic input
t = eval(input('Enter values for tuple => '))
print('Tuple t => ',t)
print('Type of t',type(t))