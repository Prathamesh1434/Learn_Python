# Differences between *args and **kwargs

# f1(*n): => *n = Tuple
# f1(**kwargs): => **kwargs = Dictonary

def f1(*n):
	print('n =>',n)
	print('Type of n =>',type(n))

f1()
f1(10,)
f1(10,20)
print()

def f2(**kwargs):
	print('kwargs =>',kwargs)
	print('Type of kwargs =>',type(kwargs))

f2()
f2(A=100)
f2(A=100,B=200)
print()

def f3(*args,**kwargs):
	print('args =>',args)
	print('Type of args =>',type(args))
	print('kwargs =>',kwargs)
	print('Type of kwargs =>',type(kwargs))

f3(10,20,A=30,B=40)

# def f4(**kwargs,*args): => Syntax error
# 	pass