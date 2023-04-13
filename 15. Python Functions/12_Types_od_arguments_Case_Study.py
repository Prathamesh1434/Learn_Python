# Defining a function.
def f1(*y,x=10): # default argument and variable length argument 
	print('Tuple y =>',y)
	print('x =>',x)

# Calling a function
f1(10,20,30,x=40) # positional argument and default argument

def f(arg1,arg2,arg3=4,arg4=8):
	print('arg1 =>',arg1)
	print('arg2 =>',arg2)
	print('arg3 =>',arg3)
	print('arg4 =>',arg4)
	print()

f(3,2)
f(10,20,30,40)
f(25,50,arg4=100)
f(arg4=2,arg1=1,arg2=4)
# f() => TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'
# f(arg3=10,arg4=20,30,40) => SyntaxError: positional argument follows keyword argument
# f(4,5,arg2=6) => TypeError: f() got multiple values for argument 'arg2'
# f(4,5,arg3=5,arg5=6) => TypeError: f() got an unexpected keyword argument 'arg5'